#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import sqlite3, re, string, codecs

def cercaterreni(f,m):

 

 c = sqlite3.connect('./data/catasto.db')
 cur = c.cursor()


 cSele = ""


 cSele += "select distinct (pa.foglio || '-' || pa.numero), pa.foglio, pa.numero, pa.progr, "
 cSele += "'<a href=\"../ll/mappa_py_dyn.html?f='" 
 cSele += "|| pa.foglio || '&m=' || pa.numero || '\"  target=\"_blank\">Loc_cart</a>',"
 cSele += "cpa.partita, cpa.classe,  cpa.redditoDomEuro, cpa.redditoAgrEuro, cod_qua.decodifica, cpa.ettari , cpa.are , cpa.centiare, (cpa.ettari * 100000 + cpa.are *100 + cpa.centiare) as mq, "
 #cSele += "giu.denominazione, per.cognome, per.nome, per.DataNascita " 

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

 cSele += "where pa.foglio =='" + f + "' and pa.numero =='" + m +"' order by pa.foglio, pa.numero, pa.subalterno, pa.progr desc"


 #if cAAAAnasc > 0:
 # cSele += "where per.cognome like '%" + cCognome + "%' and per.nome like '%" + cNome +"%' and per.DataNascita like '%" + cAAAAnasc + "%'or giu.denominazione like '%" + cDeno + "%' order by pa.foglio, pa.numero, pa.subalterno, pa.progr desc"
 #else:
 # cSele += "where per.cognome like '%" + cCognome + "%' and per.nome like '%" + cNome +"%' or giu.denominazione like '%" + cDeno + "%' order by pa.foglio, pa.numero, pa.subalterno, pa.progr desc"



 
 cur.execute(cSele)
 retrows = cur.fetchall()





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
      for col in range(0,totcol):
          table += "<td>" + str(row[col]) + "</td>"     
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
    if  (len(parametri) < 3):
        print "uso:<br> http://127.0.0.1:8080/cgi-bin/genera_html_su_fog_map_ter.py?f=0025&m=1100"

    print 'Ricerca per parametri -> '
    for key in parametri.keys():
       print "%s = %s" % (key, parametri[key].value)
 

    cercaterreni(parametri["f"].value.rjust(4,'0'), parametri["m"].value.rjust(5,'0')) 
 

if __name__ == "__main__":
    main()
