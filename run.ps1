$ErrorActionPreference = "Stop"

if (!(Test-Path ".\.venv\Scripts\Activate.ps1")) {
    Write-Error "Virtualenv não encontrada. Crie a .venv antes."
    exit 1
}

. .\.venv\Scripts\Activate.ps1

# Defaults (trata vazio e espaços)
if ([string]::IsNullOrWhiteSpace($env:STREAMLIT_SERVER_PORT)) { $env:STREAMLIT_SERVER_PORT = "8501" }
if ([string]::IsNullOrWhiteSpace($env:STREAMLIT_SERVER_ADDRESS)) { $env:STREAMLIT_SERVER_ADDRESS = "127.0.0.1" }

# Debug explícito
Write-Host "ADDR=[$($env:STREAMLIT_SERVER_ADDRESS)] PORT=[$($env:STREAMLIT_SERVER_PORT)]"

Write-Host "Iniciando Python-Labs em $($env:STREAMLIT_SERVER_ADDRESS):$($env:STREAMLIT_SERVER_PORT)"

streamlit run app.py `
  --server.address $env:STREAMLIT_SERVER_ADDRESS `
  --server.port $env:STREAMLIT_SERVER_PORT
