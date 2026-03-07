param(
  [string]$VaultPath = "./data/obsidian-vault"
)

$ErrorActionPreference = "Stop"

function Assert-Command {
  param([string]$Name)
  if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
    throw "Required command not found: $Name"
  }
}

Write-Host "[bootstrap] Checking prerequisites..."
Assert-Command "docker"
Assert-Command "python"
Assert-Command "node"
Assert-Command "npm"

$repoRoot = Join-Path $PSScriptRoot ".."
Set-Location $repoRoot

if (-not (Test-Path ".env")) {
  Copy-Item ".env.example" ".env"
  Write-Host "[bootstrap] .env created from .env.example"
}

$dataDirs = @(
  "logs",
  "data",
  "data/obsidian-vault",
  "data/nocodb",
  "data/n8n",
  "data/openwebui",
  "data/perplexica"
)
foreach ($dir in $dataDirs) {
  if (-not (Test-Path $dir)) {
    New-Item -ItemType Directory -Path $dir | Out-Null
  }
}

if ($VaultPath -and $VaultPath -ne "./data/obsidian-vault") {
  Write-Host "[bootstrap] Requested vault path: $VaultPath"
  Write-Host "[bootstrap] Update OBSIDIAN_HOST_PATH in .env if needed."
}

Write-Host "[bootstrap] Completed."
Write-Host "[bootstrap] Next: .\\scripts\\up.ps1"
