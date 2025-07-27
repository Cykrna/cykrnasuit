import psutil, requests
from flask import session

app.secret_key = "cykrna_secret_key"

def get_system_stats():
    try:
        ip = requests.get("https://api.ipify.org").text
    except:
        ip = "Offline"
    return {
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent,
        "ip": ip
    }

@app.route("/stats")
def stats():
    return get_system_stats()
