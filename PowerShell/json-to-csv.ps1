# to run .\json-to-csv.ps1 filename.csv

param([string]$file)
$filename_list = $file.Split(".")[0], "csv"
$filename_out = $filename_list -join '.'

$data = Get-Content $file -Raw
$json = $data | Out-String | ConvertFrom-Json
$csv = $json | ConvertTo-Csv -Delimiter ',' -NoTypeInformation
$clean = $csv | % { $_ -replace '","', ','} | % { $_ -replace "^`"",''} | % { $_ -replace "`"$",''}
$clean = $clean | Out-File $filename_out -Encoding "UTF8"
