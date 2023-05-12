import json

with open(f"Humano_Kamehameha.json", "r", encoding="utf-8") as j:
    datos = json.load(j)
    for x in datos:
        print(x["Datos"])