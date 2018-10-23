#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import sqlite3, re, string, codecs, os

def cercaterreni(cDeno):

    

 c = sqlite3.connect('./data/catasto.db')
 cur = c.cursor()

 cSele = "select distinct (pa.foglio || '-' || pa.numero), pa.foglio, pa.numero, pa.progr, \
 '<a href=\"../ll/mappa_py_dyn.html?f=' \
 || pa.foglio || '&m=' || pa.numero || '\"  target=\"_blank\">Loc_cart</a>', \
 cpa.partita, cpa.classe,  cpa.redditoDomEuro, cpa.redditoAgrEuro, cod_qua.decodifica, cpa.ettari, cpa.are, \
 cpa.centiare, (cpa.ettari * 100000 + cpa.are *100 + cpa.centiare) as mq, "
 cSele+="CASE "
 cSele+=" WHEN tit.tipoSoggetto='P' THEN rtrim(per.cognome||' '||per.nome||' '||indicazioniSup) "
 cSele+=" WHEN tit.tipoSoggetto='G' THEN giu.denominazione "
 cSele+="END as denominazione, "

 cSele+="CASE "
 cSele+=" WHEN tit.tipoSoggetto='P' then cmnasc.decodifica "
 cSele+="END as com_nasc, "

 cSele+="CASE "
 cSele+=" WHEN tit.tipoSoggetto='P' THEN substr(per.dataNascita,9,2)||'/'||"
 cSele+=" substr(per.dataNascita,6,2)||'/'||substr(per.dataNascita,1,4) "
 cSele+="END as data_nasc, "

 cSele+="CASE "
 cSele+=" WHEN tit.tipoSoggetto='P' THEN per.codFiscale "
 cSele+=" WHEN tit.tipoSoggetto='G' THEN giu.codFiscale "
 cSele+="END as cod_fisc, "

 cSele+="diri.decodifica||' '|| tit.titoloNonCod as diritto, "
 cSele+=" tit.quotaNum||'/'|| tit.quotaDen as quota "

 cSele += "from particella as pa "

 cSele += "left join titolarita as tit On pa.idParticella = tit.idParticella "
 cSele += "left join persona_fisica as per On tit.idSoggetto = per.idSoggetto " 
 cSele += "left join persona_giuridica as giu On tit.idSoggetto = giu.idSoggetto "
 cSele += "left join caratteristiche_particella as cpa on tit.idParticella = cpa.idParticella "
 cSele += "left join cod_qualita as cod_qua on cpa.codQualita = cod_qua.codice "
 cSele += "left join cod_comune as cmnasc on per.luogoNascita = cmnasc.codice "
 cSele += "left join cod_diritto as diri on tit.codDiritto = diri.codice "
 cSele += "where trim(per.cognome) || ' ' || trim(per.nome) like '%" + cDeno +"%' or giu.denominazione like '%" + cDeno + "%' order by pa.foglio, pa.numero, pa.subalterno, pa.progr desc"
 
 cur.execute(cSele)
 retrows = cur.fetchall()


 # Costruzione stringa sql cFrom da passare per ricerca e visualizzazione di tutti i mappali in 
 # parte cartografica cFrom=foglio in ('0025','0023') and mappale in ('1100','1256')

 # creo una lista [[fog], [map]]
 fogmap=[]
 for row in retrows:
     #FM=str(row[1]) +"-"+ str(row[2]) 
     FM=[ [str(row[1])] , [str(row[2])] ] 
     if FM not in fogmap:
          fogmap.append(FM)
     fogmaps=sorted(fogmap)
     
 FO=[]    
 cFrom=""
 for F in fogmaps:
     if F[0][0] not in FO:
          FO.append(F[0][0]) # appende il foglio
          cFrom+="foglio='" + F[0][0] + "' and mappale in ("
          for M in fogmaps: 
              if M[0][0] == F[0][0]: # che matchano il foglio
                 if len(M[1][0])>0:
                   cFrom += "" + M[1][0] + "," #scrive il mappale
          cFrom += ") or "
     cFrom = cFrom.replace(',) or ' , ') or ')
 cFrom = re.sub(r'or $', r'', cFrom) # toglie l'ultimo 'or'


 #print cFrom     
 
 
 #cFrom=""
 #ii=0
 #fogMapSql=[]
 #for row in retrows:
 #    FM= "foglio='" + str(row[1]) + "' and  mappale=" + str(row[2]) 
 #    if FM not in fogMapSql:
 #         fogMapSql.append(FM)
 #   
 #for row in fogMapSql:
 #    cFrom +=row
 #    ii=ii+1
 #    if ii < len(fogMapSql):
 #       cFrom +=" or "
        
 print "Totale mappali trovati: <b>" + str(len(fogmaps)) + "</b>"
 print "<br>"
 # print cFrom
 
 print "<a href=\"../ll/mappa_py_dyn_mappa_evi.html?cFrom|"+cFrom+'">Mappa per tutti i records trovati</a>'
 print "<br>"
 
 table = "<table>"
 table += "<tr>"
 table += "<th>fog-map</th>"
 table += "<th>fog</th><th>map</th><th>progr</th><th>Vis mappa</th><th>partita</th>"
 table += "<th>cla</th><th>Re_dom</th><th>Re_agr</th><th>qualita</th>"
 table += "<th>ettari</th><th>are</th><th>centiare</th><th>mq</th><th>Nominativo o Cognome e nome</th><th>luogo nascita</th>"
 table += "<th>data nascita</th><th>codice fiscale</th><th>titolo</th><th>percentuale</th>"
 table +="</tr>"
 

 for row in retrows:
      totcol=len(row)
      table += "<tr>"
      ncol=0
      for col in range(0,totcol):
          ncol = ncol + 1
          if col==13:
             table += "<td style='text-align:right'>" + str(row[col]) + "</td>"
          else:
             table += "<td style='text-align:center'>" + str(row[col]) + "</td>"      
      table += "</tr>"     
 table += "</table>"
 print table
 return ""


def main():
    parametri = cgi.FieldStorage()
    print "Content-Type: text/html"     # HTML is following
    print                               # blank line, end of headers


    print '<html>'
    print '<head>'    
    print '<style>'
    print 'body {background-color: #cc9966;font-family: Arial, Verdana, sans-serif;font-size: 12px;color: #000000;}'
    print 'table {background-color: #cc9966;font-family: Arial, Verdana, sans-serif;font-size: 14px;color: #000000;}'
    print 'table {border-collapse: collapse;}'
    print 'table, th, td {   border: 1px solid gray; }'
    print '</style>'
    print '</head>'
    print '<body>' 

    glofile='./data/catasto.db'
    mess=''
    if not os.path.exists(glofile):
        mess+="Manca il file -- " + glofile + '<br>'
    glofile='./data/catasto_cart_4326.sqlite'
    if not os.path.exists(glofile):
        mess+="Manca il file -- " + glofile
    if len(mess)>0:
      print mess
      return 

   
    if  (len(parametri) < 1):
        print "uso:<br> http://127.0.0.1:8080/cgi-bin/genera_html_su_terreni_mappa.py?n=comune"

    print 'Ricerca per parametri -> '
    for key in parametri.keys():
       print "%s = %s" % (key, parametri[key].value)

    cercaterreni(parametri["n"].value) 

if __name__ == "__main__":
    main()
