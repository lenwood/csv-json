#!/usr/bin/python
import json, dicttoxml, sys

# pass the filename as an argument when calling this script
if len(sys.argv) < 2:
	sys.exit('Usage: json-to-xml.py file.json')
fileIn = sys.argv[1]
fileList = [fileIn.split('.')[0], 'xml']
try:
	fileOut = sys.argv[2]
except:
	fileOut = ".".join(fileList)

# read the json file filename in
input = open(fileIn)
data = json.load(input)
input.close()

# convert to xml
xml = dicttoxml.dicttoxml(data)

# write the xml file
with open(fileOut, "wb+") as outfile:
	outfile.write(xml)
