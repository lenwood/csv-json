#!/usr/bin/python
import json, sqlite3, sys

# pass the filename as an argument when calling this script
if len(sys.argv) < 2:
	sys.exit('Usage: json-to-sqlite.py file.json')
fileIn = sys.argv[1]
fileList = [fileIn.split('.')[0], 'db']
try:
	fileOut = sys.argv[2]
except:
	fileOut = ".".join(fileList)

# read in the filename
input = open(fileIn)
jsonData = json.load(input)
input.close()

# structure the json data
jsonColumns = str(",".join(list(jsonData[0].keys())))
jsonValues = [':{0}'.format(i) for i in jsonData[0].keys()]
jsonValues = ", ".join(jsonValues)

# assemble the SQL query
query = ["INSERT INTO jsonFile VALUES (", jsonValues, ")"]
queryString = " ".join(query)

# establish connection to the database & execute the query
conn = sqlite3.connect(fileOut) # or use :memory: to put it in RAM
with conn:
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS jsonFile(" + jsonColumns + ")")
	cur.executemany(queryString, jsonData)
