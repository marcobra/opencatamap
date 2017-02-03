**Operazioni preliminari da eseguire in dipendenza del vostro sistema operativo per ottenere l'ambiente corretto all'esecuzione degli scripts python ed a rendere disponibili a python i moduli che sono necessari:**

**---- Linux**
in ubuntu 16.10 installare 

sudo apt-get install python-pyspatialite python-geojson

oppure per versioni precedenti ad esempio Ubuntu 14.04: 

sudo apt-get install python-pyspatialite

sudo pip install geojson

Se c'e' un proxy da attraversare (nel mio caso ho impostato un proxy locale con cntml per attraversare il proxy di rete)

sudo pip --proxy http://127.0.0.1:3128/ install geojson


**---- In Windows sia esso a 32 o 64 bits installare**

1) python27 a 32 bits https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi
durante l'installazione attivare l'opzione per aggiornare il path di sistema

2) installare il modulo geojson tramite easy_install.exe
c:\Python27\Scripts\easy_install.exe geojson

3) installare 7zip servirà a scompattare la libreria qui al passaggio successivo
http://www.7-zip.org/

4) scaricare e scompattare mod_spatialite
http://www.gaia-gis.it/gaia-sins/windows-bin-x86/mod_spatialite-4.3.0a-win-x86.7z
scompattarlo in una cartella ad esempio C:\sqlite3 (ma si puo' usare una cartella a piacere) 
verranno estratti una serie di file .dll e sqlite3.exe già da qui possiamo testare se il 
modulo mod_spatialite viene caricato da sqlite3 digitando:

sqlite3 -cmd "select load_extension('mod_spatialite')"
non si devono vedere messaggi di errore, digitare .exit ed invio per uscire da sqlite3.

Poi bisogna far in modo che le dll estratte possano essere caricate dinamicamente dagli script python
in particolare il file mod_spatialite.dll 
abbiamo poi adottato questa soluzione per rendere disponibili le .dll che non "sporca" il sistema più di tanto:

copiare tutti i files .dll presenti in C:\sqlite3 (vedi sopra) nella directory C:\python27\scripts\


**---- Mac**
... serve una persona con mac che possa provare a compilare sul suo pc alcune cose al fine di ottenere dettagliato howto da riportare qui
