# opencatamap
Ricerca e visualizzazione in mappa di dati catastali: urbano e catasto terreni

E' una serie di script in Python che consentono la ricerca e la visualizzazione in mappe web
dei dati catastali importati (scaricandoli dalle forniture di Sister) nel software "Visualizzazione Forniture Catastali" (da adesso VFC) e poi esportati come copia di backup appunto da VFC.

OpenCataMap e' utilizzabile con archivi catasto urbano e catasto terreni e con la cartografia catastale (terreni).

Per il catasto urbano dopo le ricerche si arriva alla visualizzazione georeferenziata del civico, questa visualizzazione è delegata a Nominatim ed alla cartografia OpenStreetMap.

Per ottenere una piena funzionalità la cartografia OpenStreetMap deve essere, e puo' essere facilmente completata, con i dati mancanti (edifici, strade, civici) da parte dell'utente, OpenStreetMap e' una mappa collaborativa e tutti possono partecipare.

Questo insieme di software e' rivolto agli uffici tecnici comunali e  alla Pubblica Amministrazione italiana, in quanto i dati che si andranno a manovrare non sono dati aperti.
In questo repository, pertanto non saranno mai distribuiti dati catastali, atti a testare l'applicazione, pertanto è necessario possedere archivi catastali di propria competenza.
