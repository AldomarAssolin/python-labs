$ErrorActionPreference = "Stop"

if (!(Test-Path ".\.venv\Scripts\Activate.ps1")) {
    Write-Error "Virtualenv não encontrada. Crie a .venv antes."
    exit 1
}

. .\.venv\Scripts\Activate.ps1

if (-not $env:STREAMLIT_SERVER_PORT) { $env:STREAMLIT_SERVER_PORT = "8501" }
if (-not $env:STREAMLIT_SERVER_ADDRESS) { $env:STREAMLIT_SERVER_ADDRESS = "8501"}

Write-Host "Iniciando Python-Labs em $env:STREAMLIT_SERVER_ADDRESS:$env:STREAMLIT_SERVER_PORT"

streamlit run app.py `
  --server.address $env:STREAMLIT_SERVER_ADDRESS `
  --server.port $env:STREAMLIT_SERVER_PORT
