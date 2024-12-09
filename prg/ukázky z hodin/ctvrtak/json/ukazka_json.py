import json

filmy = {
    "komedie": "Tropická bouře",
    "horror": ["Sinister", "IT"],
    "animak": ["Spongebob", "Lví král", "Na vlásku"],
    "muzikál": "Hamilton"
}

with open("data.json", mode="w") as soubor:
    json.dump(filmy, soubor, indent=4, ensure_ascii = False)


with open("data.json", mode="r") as soubor:
    nactena_data = json.load(soubor)

print(nactena_data)