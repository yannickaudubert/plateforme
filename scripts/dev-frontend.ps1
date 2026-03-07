param(
  [string]$Host = '0.0.0.0',
  [int]$Port = 5173
)

Set-Location "$PSScriptRoot\..\frontend"
npm install
npm run dev -- --host $Host --port $Port
