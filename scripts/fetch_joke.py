import json
import urllib.request
from datetime import datetime, timezone

URL = "https://icanhazdadjoke.com/"
req = urllib.request.Request(
    URL,
    headers={
        "Accept": "application/json",
        "User-Agent": "PracticasRedes (https://github.com/USUARIO/REPO)"
    }
)

with urllib.request.urlopen(req, timeout=10) as r:
    data = json.loads(r.read().decode("utf-8"))

out = {
    "api": "icanhazdadjoke",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "joke_id": data.get("id"),
    "joke": data.get("joke"),
    "status": data.get("status")
}

print(json.dumps(out, ensure_ascii=False, indent=2))
