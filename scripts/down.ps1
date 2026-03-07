param(
  [switch]$WithPerplexica,
  [switch]$RemoveVolumes
)

$ErrorActionPreference = "Stop"

$repoRoot = Join-Path $PSScriptRoot ".."
Set-Location $repoRoot

$composeArgs = @("-f", "docker-compose.full.yml", "down")
if ($WithPerplexica) {
  $composeArgs = @("--profile", "perplexica") + $composeArgs
}
if ($RemoveVolumes) {
  $composeArgs += "-v"
}

Write-Host "[down] Stopping stack..."
docker compose @composeArgs
Write-Host "[down] Stack stopped."
