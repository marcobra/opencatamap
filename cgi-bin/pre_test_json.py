import json

#https://pythonspot.com/json-encoding-and-decoding-with-python/

myjson="""{"risu":[
      {"foglio":"0025", "mappale": "1100"}, 
      {"foglio":"0022", "mappale": "200"},
      {"foglio":"0023", "mappale": "200"},
      {"foglio":"0024", "mappale": "200"},
      {"foglio":"0025", "mappale": "100"}
]}"""

myj = json.loads(myjson)

ii=0

nos_dict = [i for i in myj['risu'] if 'foglio' in i]
csel ="select * from Particelle where "
for item in nos_dict:
    ii = ii+1
    csel += " foglio=='" + item.get('foglio') + "' and mappale=='" + item.get('mappale')+"'"
    if ii < len(nos_dict):
       csel += " or "

print csel
