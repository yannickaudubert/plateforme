param(
  [string]$Host = '0.0.0.0',
  [int]$Port = 8000
)

Set-Location "$PSScriptRoot\..\backend"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
uvicorn app.main:app --reload --host $Host --port $Port
