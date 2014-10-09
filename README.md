Set of scripts to work with CSV & json files. I've written scrips for PowerShell & Python so far, the Python versions work better at this point. Within each folder there are the following scripts.

 - csv-to-json
 - csv-to-sqlite
 - json-to-csv
 - json-to-xml
 - json-to-sqlite
 - tsv-to-csv

In their current form they'll only work well with json files that have a flat architecture (no nested arrays or objects), but it woulnd't be difficult to extend them to handle a particular file. To use them, call the filename with the name of the file that you'd like to convert. The output file will have the same name with the updated extension. `json-to-csv.py filename.json` will produce `filename.csv`.

Use these scripts as you care to.