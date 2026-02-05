import json
import urllib.request

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

print("id:", data.get("id"))
print("status:", data.get("status"))
print("joke:", data.get("joke"))
