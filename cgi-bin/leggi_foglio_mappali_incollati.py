#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()

# legge un elenco di mappali nella forma foglio - mappale
# li trasforma e li passa a  
#
#http://127.0.0.1:8080/ll/mappa_py_dyn_mappa_evi.html?cFrom|foglio='0025' and mappale in (00035,00036,00044,00045,00046,00050)
#

#print "The user entered " % form.getvalue("datafile")

stringa = form.getfirst("incollati", "").upper() 

print('Content-type:text/html\r\n\n')
print('<!DOCTYPE HTML>')
print('<html>')
print('<body>')

aRighe=stringa.split("\r\n")
# tolgo eventuali righe nulle
aRighe=aFogMap = filter(None, aRighe) 

#casi non puliti pulisco
for rig in aRighe: 
   r=rig
   if r.count('-') > 1: # se c'e' + di una volte il car '-'
      npos=r.find('-')
      r=r[:npos]+'-'+r[npos:].replace("-",' ')
   if r.count('-') == 0: 
      r=r.replace(',','-',1) # tolgo la prima stringa , e sostituisco con "-"  
   r=r.replace('"','') # tolgo i doppi apici
   r=r.replace(',,',',') # tolgo eventuali virgole doppie
   aRighe[aRighe.index(rig)]=r # sostisco l'elemento aggiornato nell'array

#print aRighe


cFoMli=""
for rig in aRighe: 
  cFog    = " or foglio='" + rig.split("-")[0].strip().zfill(4) + "' and mappale in (" 
  cMli    = rig.split("-")[1].strip().replace('   ',' ').replace('  ',' ').replace(' ', ',') + ")"
  cMli    = cMli.replace(',,',',') # tolgo eventuali virgole doppie
  cFoMli  += cFog + cMli

cFoMli=cFoMli.lstrip(' or ') 

stringa="/ll/mappa_py_dyn_mappa_evi.html?cFrom|"+cFoMli

#print stringa

print "<script>"
print ' window.location.href="http://" + document.location.host + "' + stringa + '";'
print "</script>"

print('</body>')
print('</html>') 
