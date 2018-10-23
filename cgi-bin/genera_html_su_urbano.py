#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import sqlite3, re, string, codecs, os

def cercaurbano(cNominativo):


 c = sqlite3.connect('./data/catasto.db')
 cur = c.cursor()

 cSele = "select distinct (id_i.foglio || '-' || id_i.numero ||'-'|| id_i.subalterno), \
 '<a href=\"http://nominatim.openstreetmap.org/search/' \
 || top.decodifica || ' ' || ind.indirizzo || ' ' || ltrim(ind.civico1, '0') ||  ',16011 Arenzano\"  target=\"_blank\">W_osm </a>', \
 '<a href=\"../osmlocation/dettaglio-mappa.htm?location=' \
 || top.decodifica || ' ' || ind.indirizzo || ' ' || ltrim(ind.civico1, '0') ||  ',16011 Arenzano\"  target=\"_blank\"> L_osm </a>', \
 id_i.foglio, id_i.numero, id_i.subalterno, id_i.progr, \
 ui.categoria, ui.classe, ui.renditaEuro, (top.decodifica || ' ' || ind.indirizzo || ' ' || ind.civico1), \
 giu.denominazione, per.cognome, per.nome, per.DataNascita \
 from identificativi_immobiliari as id_i \
 left join indirizzi as ind On id_i.idImmobile = ind.idImmobile \
 left join titolarita as tit On id_i.idImmobile = tit.idImmobile \
 left join persona_fisica as per On tit.idSoggetto = per.idSoggetto \
 left join persona_giuridica as giu On tit.idSoggetto = giu.idSoggetto \
 left join unita_immobiliari as ui on tit.idImmobile = ui.idImmobile \
 left join cod_toponimo as top on ind.toponimo = top.codice \
 where trim(per.cognome) || ' ' || trim(per.nome) like '%" + cNominativo + "%' or giu.denominazione like '%" + cNominativo + "%' group by id_i.foglio, id_i.numero, id_i.subalterno order by id_i.foglio, id_i.numero, id_i.subalterno, id_i.progr desc"

 #print cSele

 cur.execute(cSele)
 retrows = cur.fetchall()

 table = "<table>"
 table += "<tr>"
 table += "<th>fog-map-sub</th><th>nominatim</th><th>loc_via_norm</th>"
 table += "<th>fog</th><th>map</th><th>sub</th><th>progr</th><th>cat</th>"
 table += "<th>cla</th><<th>rend</th><th>Indirizzo</th><th>Cognome</th><th>Nome</th><th>data_nascita</th>"
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
    print 'body {background-color: #ccff66;font-family: Arial, Verdana, sans-serif;font-size: 12px;color: #000000;}'
    print 'table {background-color: #ccff66;font-family: Arial, Verdana, sans-serif;font-size: 14px;color: #000000;}'
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
        print "uso:<br> http://127.0.0.1:8080/cgi-bin/genera_html_su_urbano.py?N=Dam"

    print 'Ricerca per parametri -> '
    for key in parametri.keys():
       print "%s = %s" % (key, parametri[key].value)


   
    cercaurbano(parametri["n"].value)
    
if __name__ == "__main__":
    main()
