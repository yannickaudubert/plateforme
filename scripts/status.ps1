param(
  [switch]$WithPerplexica
)

$ErrorActionPreference = "Stop"

function Test-Url {
  param([string]$Name, [string]$Url)
  try {
    $response = Invoke-WebRequest -Uri $Url -Method GET -TimeoutSec 4 -UseBasicParsing
    Write-Host ("[status] {0}: OK ({1})" -f $Name, $response.StatusCode)
  } catch {
    Write-Host ("[status] {0}: DOWN ({1})" -f $Name, $_.Exception.Message)
  }
}

$repoRoot = Join-Path $PSScriptRoot ".."
Set-Location $repoRoot

$composeArgs = @("-f", "docker-compose.full.yml", "ps")
if ($WithPerplexica) {
  $composeArgs = @("--profile", "perplexica") + $composeArgs
}

docker compose @composeArgs

Write-Host ""
Write-Host "[status] HTTP probes"
Test-Url -Name "frontend" -Url "http://localhost:5173"
Test-Url -Name "backend" -Url "http://localhost:8000/health"
Test-Url -Name "nocodb" -Url "http://localhost:8080"
Test-Url -Name "n8n" -Url "http://localhost:5678"
Test-Url -Name "openwebui" -Url "http://localhost:3000"
if ($WithPerplexica) {
  Test-Url -Name "perplexica" -Url "http://localhost:3001"
}
