import re
import string
def clean_str(text):
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
  
  return text

for i in range(len(phrases)):
  phrases.iloc[i] = clean_str(phrases.iloc[i])