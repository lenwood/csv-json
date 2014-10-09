#!/usr/bin/python
import csv, sqlite3, sys

# pass the filename as an argument when calling this script
if len(sys.argv) < 2:
	sys.exit('Usage: tsv-to-csv.py file.tsv')
filename_in = sys.argv[1]
filename_list = [filename_in.split('.')[0], 'csv']
filename_out = ".".join(filename_list)

with open(filename_in, 'rU') as tsvin, open(filename_out, 'wb+') as csvout:
	tsvin = csv.reader(tsvin, delimiter='\t')
	csvout = csv.writer(csvout)
	for item in tsvin:
		csvout.writerow(item)