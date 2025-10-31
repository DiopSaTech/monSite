# update_data.py
import json
import requests
from datetime import datetime

# Ici, tu pourrais scraper TIOBE ou utiliser une autre source
# Pour l'exemple, on garde des données simulées
data = {
    "labels": ["Jan", "Fév", ..., "Déc"],
    "datasets": [ ... ]  # tes données
}

with open("data/lang_stats.json", "w") as f:
    json.dump(data, f)