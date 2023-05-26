from tensorflow.keras.preprocessing.text import Tokenizer
#scrivi qui il codice
#chiamiamo l'istanza di Tokenizer inizializzandola
tokenizer=Tokenizer() 

tokenizer.fit_on_texts(phrases)
#vocabolario di parole
len(tokenizer.word_index)    
sequence_phrases = tokenizer.texts_to_sequences(phrases)