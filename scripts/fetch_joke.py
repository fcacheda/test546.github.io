import requests
import json
from datetime import datetime, timezone

URL = "https://icanhazdadjoke.com/"

headers = {
    "Accept": "application/json",
    # Es importante enviar un User-Agent identificable
    "User-Agent": "PracticasRedes (https://github.com/USUARIO/REPO)"
}

response = requests.get(URL, headers=headers, timeout=10)

# Lanza excepción si la respuesta no es 2xx
response.raise_for_status()

data = response.json()

out = {
    "api": "icanhazdadjoke",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "joke_id": data.get("id"),
    "joke": data.get("joke"),
    "status": data.get("status")
}

# Imprime JSON formateado (ideal para redirigir a fichero en GitHub Actions)
print(json.dumps(out, ensure_ascii=False, indent=2))
