param(
  [switch]$WithPerplexica
)

$ErrorActionPreference = "Stop"

$repoRoot = Join-Path $PSScriptRoot ".."
Set-Location $repoRoot

if (-not (Test-Path ".env")) {
  Write-Host "[up] .env missing, running bootstrap..."
  & "$PSScriptRoot/bootstrap.ps1"
}

$composeArgs = @("-f", "docker-compose.full.yml", "up", "-d", "--build")
if ($WithPerplexica) {
  $composeArgs = @("--profile", "perplexica") + $composeArgs
}

Write-Host "[up] Starting stack..."
docker compose @composeArgs

Write-Host "[up] Stack started."
Write-Host "[up] Check status with: .\\scripts\\status.ps1"
