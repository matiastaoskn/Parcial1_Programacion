import csv

with open("nuevo.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    for personaje in lista:
        lista_habilidades = []
        razas = personaje["Raza"][0]
        
        if filtro == razas:
            nombre = personaje['Nombre']
            poder_Pelea = int(personaje["PoderdePelea"]) * 0.5
            poderAtaque = int(personaje["PoderdeDefensa"]) * 0.7
        
            for habilidad in personaje["Habilidades"]:
                lista_habilidades.append(habilidad)
            lista_habilidades.append("transformación nivel dios")
            
            writer.writerow(lista_habilidades)
            writer.writerow([nombre])
            writer.writerow([poder_Pelea])
            writer.writerow([poderAtaque])
