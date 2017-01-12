# opencatamap
Ricerca e visualizzazione in mappa di dati catastali: urbano e catasto terreni

E' una serie di script in Python che consentono la ricerca e la visualizzazione in mappe web
dei dati catastali importati (scaricandoli dalle forniture di Sister) nel software "Visualizzazione Forniture Catastali" (da adesso VFC) e poi esportati come copia di backup appunto da VFC.

Funziona per catasto urbano e catasto terreni.

Per il catasto urbano dopo le ricerche si arriva alla visualizzazione georeferenziata del civico, questa visualizzazione è delegata a Nominatim ed alla cartografia OpenStreetMap.

Per ottenere una piena funzionalità la cartografia OpenStreetMap deve essere, e puo' essere facilmente completata, con i dati mancanti (edifici, strade, civici) da parte dell'utente, OpenStreetMap e' una mappa collaborativa e tutti possono partecipare.

Questo insieme di software e' rivolto agli uffici tecnici comunali e comunque alla Pubblica Amministrazione italiana in quanto i dati che si andranno a manovrare non sono dati aperti.

In questo reposistory pertanto non troverete mai dati catastali con i quali potrete testare l'applicazione.
