import requests
import json
from datetime import datetime, timezone
import os

BASE_URL = "https://api.nasa.gov/planetary/apod"

# La API key se obtiene del entorno (GitHub Actions) o se puede usar DEMO_KEY en local
NASA_API_KEY = os.environ.get("NASA_API_KEY", "DEMO_KEY")

params = {
    "api_key": NASA_API_KEY
}

response = requests.get(BASE_URL, params=params, timeout=15)

# Lanza excepción si la respuesta HTTP no es 2xx
response.raise_for_status()

data = response.json()

out = {
    "api": "NASA APOD",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "date": data.get("date"),
    "title": data.get("title"),
    "explanation": data.get("explanation"),
    "media_type": data.get("media_type"),
    "url": data.get("url"),
    "hdurl": data.get("hdurl"),
    "copyright": data.get("copyright")
}

# Imprime JSON formateado (ideal para redirigir a fichero en GitHub Actions)
print(json.dumps(out, ensure_ascii=False, indent=2))
