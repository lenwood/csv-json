#!/usr/bin/python
import csv, os, sqlite3, sys

# pass the filename as an argument when calling this script
if len(sys.argv) < 2:
	sys.exit('Usage: csv-to-sqlite.py /path/to/file.csv')
fileIn = sys.argv[1]
fileOnly = os.path.basename(fileIn)
try:
	fileOut = sys.argv[2]
except:
	fileList = [fileOnly.split('.')[0], 'db']
	fileOut = ".".join(fileList)

# read the file
data = csv.reader(open(fileIn, 'rU'), delimiter=',')

# structure the csv data
csvHeaderRow = data.next()
csvHeaders = ", ".join(str(i) for i in csvHeaderRow)
csvValues = [":{0}".format(j) for j in csvHeaderRow]
csvValues = ", ".join(csvValues)

# build the query
query = ["INSERT INTO csvFile VALUES (", csvValues, ")"]
queryString = " ".join(query)

# connect to the database & execute the query
conn = sqlite3.connect(fileOut)
with conn:
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS csvFile(" + csvHeaders + ")")
	cur.executemany(queryString, data)