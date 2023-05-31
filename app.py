from flask import Flask, render_template
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from keras.utils import pad_sequences
import re
import string
from tensorflow.keras.preprocessing.text import Tokenizer


app = Flask(__name__)
pagina = 'npl.html'

#da importare csv per definire df


@app.route("/lemming")
def lemming_e_rimozione_sto_words():
    #codice per definire le stopword ed inizializzare il lemmatizer
    # Stop words
    nltk.download('stopwords')
    stop=stopwords.words('english')
    # Lemmatizer
    nltk.download("wordnet") 
    lemmatizer = WordNetLemmatizer()

    for i in range(len(phrases)):
    #assegno ad una nuova variabile "sentence" la frase all'interno di text con indice i (utilizzare la funzione iloc)
    sentence = phrases.iloc[i]
    
    #divido la fase nelle parole che la compongono
    sentence = sentence.split(' ')
    #dichiaro una nuova variabile
    newSentence = []
    for w in sentence:
        #lemmatizzo w 
        w = lemmatizer.lemmatize(w)
        #controllo se w non è una stop word
        if w not in stop:
        #se non lo è allora aggiungo w alla variabile definita sopra
            newSentence.append(w)
    phrases.iloc[i] = ' '.join(newSentence)
    return render_template(pagina, text=list(phrases))


@app.route("/tokenization")
def padding_con_keras():
    return render_template(pagina, text = ' ') #da completare

@app.route("/pulizia.py")
def pulizia_testo():
    return render_template(pagina, text = ' ') #da completare

@app.route("/sequence")
def tokenization_e_sequence_con_keras():
    return render_template(pagina, text = ' ') #da completare