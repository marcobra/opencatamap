# opencatamap
Ricerca e visualizzazione in mappa di dati catastali: urbano e catasto terreni

E' una serie di script in Python che consentono la ricerca e la visualizzazione in mappe web
dei dati catastali prima importati (scaricandoli dalle forniture di Sister) nel software "Visualizzazione Forniture Catastali" (da ora abbreviato in VFC) e poi esportati come copia di backup appunto da VFC. ( opencatamap/data/catasto.db )

OpenCataMap e' utilizzabile con archivi catasto urbano e catasto terreni.
Si avvale della cartografia catastale (particelle terreni) che viene usata per le visualizzazioni, sovrapposizioni a livelli di mappe di base.

Detta cartografia, al primo impianto del software e poi nei successivi aggiornamenti, deve essere importata in qgis tramite il plugin cxf_in ed esportata poi in un file spatialite, il file che viene usato per la visualizzazione dei dettagli cartografici.
( opencatamap/data/catasto_cart_4326.sqlite )

Le mappe di base sono personalizzabili, e' pertanto possibile visualizzare delle tiles prodotte dalla Cartografia Tecnica Regionale CTR del vostro comune.
La CTR deve essere georeferenziata e va' trasformata in tiles (in Linux con gdal2tiles) che poi andranno poste nella cartella custom_tiles dell'ambiente. ( opencatamap/cust_tiles/ctr )

Per il catasto urbano dopo le ricerche si arriva alla visualizzazione georeferenziata del civico, questa visualizzazione è delegata a Nominatim ed alla cartografia OpenStreetMap.

Per ottenere una piena funzionalità la cartografia OpenStreetMap deve essere, e puo' essere facilmente completata, con i dati mancanti (edifici, strade, civici) da parte dell'utente, OpenStreetMap e' una mappa collaborativa e tutti possono partecipare.

Questo insieme di software e' rivolto agli uffici tecnici comunali e  alla Pubblica Amministrazione italiana, in quanto i dati che si andranno a manovrare non sono dati aperti.
In questo repository, pertanto non saranno mai distribuiti dati catastali, atti a testare l'applicazione, pertanto è necessario possedere archivi catastali di propria competenza.

Questo software non prevede installazioni di webserver neppure di dbserver particolari ed e' pensato per essere usato sul singolo pc o anche in una piccola rete locale in tal caso sul pc dovrà essere avere attivo un firewall che garantirà l'accesso via web solo agli ip abilitati.

All'applicazione si accede: in locale via web da 127.0.0.1:8080, o da altro pc in rete da 192.168.X.X:8080

Il software richiede l'installazione di Python sul pc, ed anche altri moduli python, deve essere installato anche il modulo  
https://www.gaia-gis.it/fossil/libspatialite/wiki?name=mod_spatialite atto alla visualizzazione delle mappe, su certi sistemi operativi (in Mac osx e versioni di Ubuntu inferiori alla 16.04) è necessario compilare questo modulo da sorgenti (sono gradite smentite).

Cio' che è richiesto per il funzionamento, sui vari sistemi: Linux, Mac, Windows verrà specificato in dettaglio prossimamente.

Per ora (16 gen 2017) il software pur essendo funzionante ( testato su Ubuntu Linux ed anche su windows 8 e windows 10), non viene ancora distribuito tramite github, il programma necessita ancora di un affinamento che che lo renda fruibile nel modo più semplice possibile su tutti i sistemi.


