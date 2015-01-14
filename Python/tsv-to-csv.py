#!/usr/bin/python
import csv, os, sqlite3, sys

# pass the filename as an argument when calling this script
if len(sys.argv) < 2:
	sys.exit('Usage: tsv-to-csv.py file.tsv')
fileIn = sys.argv[1]
fileOnly = os.path.basename(fileIn)
try:
	fileOut = sys.argv[2]
except:
	fileList = [fileOnly.split('.')[0], 'csv']
	fileOut = ".".join(fileList)

with open(fileIn, 'rU') as tsvin, open(fileOut, 'wb+') as csvout:
	tsvin = csv.reader(tsvin, delimiter='\t')
	csvout = csv.writer(csvout)
	for item in tsvin:
		csvout.writerow(item)