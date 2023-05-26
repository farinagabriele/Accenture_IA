from keras.utils import pad_sequences
# calcolo massima lunghezza delle parole
vocab_size = len(tokenizer.word_index) + 1
maxlen=0
for phrase in sequence_phrases:
  if maxlen<len(phrase):
    maxlen=len(phrase)

padding_phrases = pad_sequences(sequence_phrases, padding='post', maxlen=maxlen)