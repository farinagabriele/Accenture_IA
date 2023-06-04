# Accenture Artificial Intelligence project

Questo è il progetto finale di un'attività di alternanza scuola-lavoro svolta in collaborazione con l'azienda Accenture

## Autori

Farina Gabriele, Floridi Matteo, Charles Matias, Rea Patryk.

## Descrizione del progetto

E' una web app che interagisce con un'*ANN* (Artificial Neural Network) di *NPL* (Natural Processing Language)
Dato in input un testo, l'app mostra passo dopo passo il *text pre-processing* ed il risultato della **predizione** dell'ANN al click di ciascun bottone

## Tecnologie utilizzate

Server-side:
- **Flask**: un framework di Python che consente la creazione di *micro-server*;
- **Jinja2**: un motore grafico che consente la creazione dinamica di pagine *HTML*, tramite l'utilizzo di codice Python.
Client-side:
- **AJAX**: Asynchronus Javascript And XML è una tecnica che consente di effettuare *chiamate asincrone* al server, quindi consente di effettuare elaborazione server-side senza il bisogno di ricaricare la pagina.
Ogni clik di un bottone effettua un'**AJAX**.

## Descrizione dei file e delle cartelle

- *./app.py*: è il *micro-server* creato con **Flask**.
- *./requirements.txt*: contiene l'elenco di tutti i package utilizzati.
- *sentiment_analysis.h5*: è l'*ANN* esportata.
- *amazon_cells_labelled.txt*: è un file *TSV* (Tab Separated Value) che contiene il database delle frasi su cui è stata addestrata l' *ANN*: la prima colonna contiene le frasi, la seconda le etichette. 0 corrisponde ad una frase pessimistica, 1 ad una ottimistica.

### ./templates

Contiene le pagine HTML dinamiche:
- *./templates/layout.html*: è il tema utilizzato nella web app.
- *./templates/index.html*: è la schermata della web app.
- *./templates/npl.html*: è la pagina *renderizzata* come risposta alla pressione dei bottoni "Pulizia Testo" e "Lemming".
- *./templates/answer.html*: è la pagina *renderizzata* come risposta alla pressione del bottone "Answer".

### ./static

Contiene i fogli di stile e gli script scritti in Javascript, eventualmente anche le immagini, ovvero tutto ciò che è statico in una web app:
- *./static/script.js*: contiene la funzione che effettua l'**AJAX**.
- *./static/style.css*: contiene lo stile della web app.

## Come eseguire il progetto in locale (Windows e Linux)

1. Installare Python 3.10
2. Clonare la repository con il comando:
```
$ git clone git@github.com:farinagabriele/Accenture_IA.git
```
Oppure scaricare il file zip e decomprimerlo dal link:

[github.com/farinagabriele/Accenture_IA](https://github.com/farinagabriele/Accenture_IA)

3. Entrare nella cartella del progetto con il comando:
```
$ cd Accenture_IA
```
4. Installare i package necessari con il comando: 
```
$ pip install -r requirements.txt
```
5. Eseguire il file *app.py* con il comando:
```
$ python app.py
```
