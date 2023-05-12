import csv
for personaje in lista:
        lista_habilidades = []
        razas = personaje["Raza"][0]
        if filtro == razas:
            print(f"Nombre: {personaje['Nombre']}")
            poder_Pelea = int((personaje["PoderdePelea"]) * 0.5) + int(personaje["PoderdePelea"])
            poderAtaque = int((personaje["PoderdeDefensa"]) * 0.7) + int(personaje["PoderdeDefensa"])
        for habilidad in personaje["Habilidades"]:
            lista_habilidades.append(habilidad)
            lista_habilidades.append("transformación nivel dios")
            with open("nuevo.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(lista_habilidades)
