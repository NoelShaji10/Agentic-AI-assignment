import os

import requests


api_key = os.getenv("GROQ_API_KEY")
headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
resp = requests.get("https://api.groq.com/openai/v1/models", headers=headers, timeout=30).json()

if "data" in resp:
    models = [m["id"] for m in resp["data"]]
    with open("models.txt", "w") as f:
        f.write("\n".join(models))
