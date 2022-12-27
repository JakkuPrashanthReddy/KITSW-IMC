mkdir -p ~/.streamlit/
echo "[theme]
base='light'
primaryColor='#004265'
font = 'sans serif'
[server]
headless = true
port = $PORT
maxUploadSize=10
enableXsrfProtection=false
enableCORS = false
" > ~/.streamlit/config.toml
