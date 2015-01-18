# to run ./xml-to-csv.ps1 filename.xml

param([string]$file)
$filename_list = $file.Split(".")[0], "csv"
$filename_out = $filename_list -join '.'

$data = Get-Content $file
$data.Sites.ChildNodes | Export-Csv $filename_out -NoTypeInformation -Delimiter:"," -Encoding:UTF8