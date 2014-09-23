param([string]$file)
$filename_list = $file.split(".")[0], "xml"
$filename_out = $filename_list -join '.'

$data = Get-Content $file -Raw
$json = $data | Out-String | ConvertFrom-Json
$xml = $json | ConvertTo-XML -NoTypeInformation -As String
$xml | Out-File $filename_out -Encoding "UTF8"
