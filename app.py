import re
import string
from flask import Flask, render_template
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from keras.utils import pad_sequences
from keras.preprocessing.text import Tokenizer
import pandas as pd
import numpy as np
from keras.models import load_model



app = Flask(__name__)

# Set templates to auto-reload
app.config["TEMPLATES_AUTO_RELOAD"] = True

PAGINA = 'npl.html'

df_am = pd.read_csv("./amazon_cells_labelled.txt",sep='\t',names=['phrase','label'])

tokenizer = Tokenizer()
sequence_phrases = []

# da importare csv per definire df
phrases = df_am['phrase']
label = df_am['label']

# rete neurale
model = load_model("sentiment_analysis.h5")




@app.route("/answer", methods=["GET"])
def answer():
    return model.predict(txt)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/lemming", methods=["GET"])
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
            # se non lo è allora aggiungo w alla variabile definita sopra
                newSentence.append(w)
    phrases.iloc[i] = ' '.join(newSentence)
    return render_template(PAGINA, text=list(phrases))


@app.route("/tokenization", methods=["GET"])
def padding_con_keras():
    vocab_size = len(tokenizer.word_index) + 1
    maxlen=0
    for phrase in sequence_phrases:
        if maxlen<len(phrase):
            maxlen=len(phrase)
    padding_phrases = pad_sequences(sequence_phrases, padding='post', maxlen=maxlen)
    return render_template(PAGINA, text = ' ') #da completare


def pulizia_testo(text):
    #inserire qui pulizia del testo
    # Elimino siti web
    text = text.lower()
    text = re.sub("http://([a-z])*[.]([a-z])*[.]([a-z])*", "", text)
    # Elimino la punteggiatura
    for c in string.punctuation:
        text = text.replace(c, "")
    # Elimino i numeri
    text = re.sub("\d","",text)
    text = text.replace("  ", " ")
    text = text.replace("   ", " ")

    return render_template(PAGINA, text = text) 


@app.route("/sequence", methods=["GET"])
def tokenization_e_sequence_con_keras():
    tokenizer.fit_on_texts(phrases)
    #vocabolario di parole
    len(tokenizer.word_index)    
    sequence_phrases = tokenizer.texts_to_sequences(phrases)
    return render_template(PAGINA, text = ' ') #da completare