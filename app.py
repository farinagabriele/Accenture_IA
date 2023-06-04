import re
import string
from flask import Flask, render_template, request
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from keras.utils import pad_sequences
from keras.preprocessing.text import Tokenizer
import pandas as pd
import numpy as np
from keras.models import load_model
from keras.optimizers import Adam


''' Configurazione dell'app '''
app = Flask(__name__)
# Set templates to auto-reload
app.config["TEMPLATES_AUTO_RELOAD"] = True
PAGINA = 'npl.html'
''' Download dei package nltk '''
#nltk.download('stopwords')
#nltk.download("wordnet")

''' Caricamento e compilazione dell'ANN '''
model = load_model("sentiment_analysis.h5")
lr = 0.0001
model.compile(optimizer=Adam(learning_rate=lr), run_eagerly=True)


@app.route("/pulizia", methods=["GET"])
def pulizia():
    ''' Questa route pulisce il testo dalla punteggiatura, dai numeri e dai siti web. '''
    if request.args.get("text"):
        txt = request.args.get("text")
        txt = pulizia_testo(txt)
        return render_template(PAGINA, text=txt)
    
    else:
        return render_template(PAGINA)    


@app.route("/", methods=["GET"])
def index():
    ''' Questa route renderizza la pagina principale. '''
    return render_template("index.html")


@app.route("/lemming", methods=["GET"])
def lemming_e_rimozione_sto_words():
    ''' Questa route lemmatizza il testo e rimuove le stop words. '''
    if request.args.get("text"):
        txt = request.args.get("text")
        # codice per definire le stopword ed inizializzare il lemmatizer
        # Stop words
        stop=stopwords.words('english')
        # Lemmatizer 
        lemmatizer = WordNetLemmatizer()
        # assegno ad una nuova variabile "sentence" la frase all'interno di text con indice i (utilizzare la funzione iloc)
        sentence = txt
        # divido la fase nelle parole che la compongono
        sentence = sentence.split(' ')
        # dichiaro una nuova variabile
        newSentence = []
        for w in sentence:
            # lemmatizzo w 
            w = lemmatizer.lemmatize(w)
            # controllo se w non è una stop word
            if w not in stop:
            # se non lo è allora aggiungo w alla variabile definita sopra
                newSentence.append(w)

        txt = ' '.join(newSentence)
        return render_template(PAGINA, text=txt)
    else:
        return render_template(PAGINA)


def pulizia_testo(text):
    ''' Questa funzione pulisce il testo dalla punteggiatura, dai numeri e dai siti web. '''
    text = text.lower()
    text = re.sub("http://([a-z])*[.]([a-z])*[.]([a-z])*", "", text)
    # Elimino la punteggiatura
    for c in string.punctuation:
        text = text.replace(c, "")

    # Elimino i numeri
    text = re.sub("\d","",text)
    text = text.replace("  ", " ")
    text = text.replace("   ", " ")

    return render_template(PAGINA, text=text) 


@app.route("/tokenization", methods=["GET"])
def tokenization_e_sequence_con_keras():
    ''' Questa route tokenizza il testo, crea le sequenze di numeri ed effettua una predizione con l'ANN. '''
    if request.args.get("text"):
        tokenizer = Tokenizer()
        txt = str(request.args.get("text"))
        maxL = 16
        txt = [txt]
        tokenizer.fit_on_texts(txt)
        #vocabolario di parole
        len(tokenizer.word_index)
        # trasformo le parole in sequenze di numeri   
        sequence_phrases = tokenizer.texts_to_sequences(txt)
        # calcolo massima lunghezza delle parole
        padding_txt = pad_sequences(sequence_phrases, padding='post', maxlen=maxL)
        X = padding_txt
        prediction = model.predict(X)
        return render_template('answer.html', sequence=sequence_phrases, index=tokenizer.word_index, padding=str(padding_txt), answer=prediction)
    else:
        return render_template(PAGINA)


if __name__ == '__main__':
    ''' Avvio dell'app '''
    app.run(debug=True, port=8040)
