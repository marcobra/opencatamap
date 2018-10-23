#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()

# legge un elenco di mappali nella forma foglio - mappale
# li trasforma e li passa a  
#
#http://127.0.0.1:8080/ll/mappa_py_dyn_mappa_evi.html?cFrom|foglio='0025' and mappale in (00035,00036,00044,00045,00046,00050)
#

#print "The user entered " % form.getvalue("datafile")

stringa = form.getfirst("datafile", "").upper() 

print('Content-type:text/html\r\n\n')
print('<!DOCTYPE HTML>')
print('<html>')
print('<body>')
#for item in form.getlist("datafile"):
#    print item + "<br>"
#print(stringa)

aFogMap=stringa.split('\r\n') # nel caso di un file terminato con cr+lf
#print len(aFogMap)
if len(aFogMap)< 2:  #se non ha gia' creato l'array da un file windows prova a vedere se e' un file unix
   aFogMap=stringa.split('\n') # nel caso unix solo  newline
#tolgo eventuali valori nulli
aFogMap = filter(None, aFogMap) 
#sorto la lista
aFogMapS=sorted(aFogMap)


#creo array del solo campo foglio 
aFogli=[fogmap.split("-")[0].zfill(4) for fogmap in aFogMapS]
#tolgo i valori duplicati
aFogliUnici = list(set(aFogli))

#print aFogliUnici

stringa="/ll/mappa_py_dyn_mappa_evi.html?cFrom|foglio='"
for fu in aFogliUnici:
    stringa+=fu+"' and mappale in("
    i=0
    while i < len(aFogMapS):
      myf=aFogMapS[i].split("-")[0].zfill(4)
      mym=aFogMapS[i].split("-")[1]
      if fu == myf:
          stringa+= mym + "," 
      i += 1 
    stringa+=") or foglio='"
stringa += ')'
stringa=stringa.replace(',)',')')   
stringa=stringa.replace(" or foglio=')","")   
#print stringa

print "<script>"
print ' window.location.href="http://" + document.location.host + "' + stringa + '";'
print "</script>"

print('</body>')
print('</html>') 
