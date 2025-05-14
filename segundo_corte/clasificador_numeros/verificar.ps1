# verificar.ps1

# Ejecutar el script Python
python main.py --archivo input.txt

# Leer los archivos
$expected = Get-Content expected_output.txt
$output = Get-Content output.txt

# Comparar contenido
$diferencias = Compare-Object $expected $output

if ($diferencias) {
    Write-Host "[ERROR] Las salidas NO coinciden. Revisa las diferencias:" -ForegroundColor Red
    $diferencias
} else {
    Write-Host "[OK] Las salidas coinciden. Prueba exitosa." -ForegroundColor Green
}
