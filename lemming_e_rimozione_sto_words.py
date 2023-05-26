import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
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
