# to run ./csv-to-json.ps1 filename.csv

param([string]$file)
$filename_list = $file.Split(".")[0], "json"
$filename_out = $filename_list -join '.'

$data = Get-Content $file
$new = $data | ConvertFrom-Csv -Delimiter ',' | ConvertTo-Json | Out-File $filename_out -Encoding "UTF8"
