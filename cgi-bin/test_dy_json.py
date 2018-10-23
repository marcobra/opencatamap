#!/usr/bin/python
# -*- coding: utf-8 -*-

#from pyspatialite import dbapi2 as db
#import pyspatialite.dbapi2 as db
import csv, os, sys, cgi
import sqlite3
import geojson

# prende dei parametri passati fog e map
parametri = cgi.FieldStorage()
myjson=parametri["json"].value


# create a new Spatialite database file (and delete any existing of the same name)
if os.path.exists('catasto_cart_4326.sqlite'):
    #os.remove('MyDatabase.sqlite')
    conn = sqlite3.connect('catasto_cart_4326.sqlite')

# load spatialite extensions for SQLite.
# on Windows: make sure to have the mod_spatialite.dll somewhere in your system path.
# on Linux: to my knowledge the file is called mod_spatialite.so and also should be located in a directory 
# available in your system path.
# on uuntu install 
# sudo apt-get install libsqlite3-mod-spatialite

# vedere http://gis.stackexchange.com/questions/142970/dump-a-geojson-featurecollection-from-spatialite-query-with-python

conn.enable_load_extension(True)
conn.execute('SELECT load_extension("mod_spatialite.so")')


# create a new table and fill it with some example values
createTableQuery = """
CREATE TABLE
    MyTable(
            geometry,
            firstAttribute,
            secondAttribute,
            thirdAttribute
            )
;
"""

fillTableQuery = """
INSERT INTO
    MyTable(
            geometry,
            firstAttribute,
            secondAttribute,
            thirdAttribute
            )
VALUES
    (
        GeomFromText('POINT(10 20)', 4326), 15, 'some Text', 'some other Text'
    )
;
"""
#myFog='0020'
#myMap='2'

mytestjson='{
    "foglio": 25,
    "mappale": "1100",
    "foglio": 22,
    "mappale": 200
}'

myjson=mytestjson
import json
j = json.loads(myjson)
print j['foglio']
#print myjson

#costruisce la query dal json passato come argomento json e' in forma foglio-mappale, foglio-mappale e serve per ottenere 
#poi una visualizzazione di più di una particella viene passato dalla pagina di ricerca del possessore dei terreni


getResultsQuery = """
SELECT
    AsGeoJSON(geometry),
    foglio,
    mappale
FROM
    Particelle where foglio=='""" + myFog + """' and mappale=='""" + myMap.lstrip('0') + """'
;
"""


# function that makes query results return lists of dictionaries instead of lists of tuples
def dict_factory(cursor, row):
    d = {}
    for idx,col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# apply the function to the sqlite3 engine
conn.row_factory = dict_factory

# fetch the results in form of a list of dictionaries
results = conn.execute(getResultsQuery).fetchall()

# create a new list which will store the single GeoJSON features
featureCollection = list()

# iterate through the list of result dictionaries
for row in results:

    # create a single GeoJSON geometry from the geometry column which already contains a GeoJSON string
    geom = geojson.loads(row['AsGeoJSON(geometry)'])

    # remove the geometry field from the current's row's dictionary
    row.pop('AsGeoJSON(geometry)')

    # create a new GeoJSON feature and pass the geometry columns as well as all remaining attributes which are stored in the row dictionary
    feature = geojson.Feature(geometry=geom, properties=row)

    # append the current feature to the list of all features
    featureCollection.append(feature)

# when single features for each row from the database table are created, pass the list to the FeatureCollection constructor which will merge them together into one object
featureCollection = geojson.FeatureCollection(featureCollection)

# print the FeatureCollection as string
#GeoJSONFeatureCollectionAsString = geojson.dumps(featureCollection)
#print(GeoJSONFeatureCollectionAsString)

# Per far si che venga letto il responso come html geojson dagli script leaflet
print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers


# print the FeatureCollection as string indented

GeoJSONFeatureCollectionAsString = geojson.dumps(featureCollection, indent=2)
print(GeoJSONFeatureCollectionAsString)


#conn.execute(createTableQuery)
#conn.execute(fillTableQuery)


conn.commit()
