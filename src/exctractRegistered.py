from pathlib import Path
from datetime import datetime
from datetime import date
import json

# chemin vers la racine du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# chemin vers le fichier json
DATA_FILE = BASE_DIR / "data" / "data.json"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)


def PrintItems():
    # Getting the data part
    listExpired = []
    listNotExpired = []

    for item in data:
        expiration_date = datetime.strptime(item["date"], "%d/%m/%Y")
        expired = expiration_date < datetime.now()
        if expired:
            listExpired.append(item)
        else:
            listNotExpired.append(item)
            distanceFromExpiration = (expiration_date.date() - date.today()).days
            item.update({"days_until_expiration": distanceFromExpiration})

    listNotExpired.sort(key=lambda x: x["days_until_expiration"])

    # Printing the results
    print("\nExpired items:")
    for expired_item in listExpired:
        print("Name:", expired_item["name"], "| Expiration Date:", expired_item["date"])
    print("\nNot expired items:")
    for not_expired_item in listNotExpired:
        print(
            "Name:",
            not_expired_item["name"],
            "| Expiration Date:",
            not_expired_item["date"],
            "| Days until expiration:",
            not_expired_item["days_until_expiration"],
        )
    print("\n")
