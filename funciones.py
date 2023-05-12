import re
import random
import datetime
import json

from main import jason_Existe
#1
def Traerdatosdesdearchivo():
    with open("Parcial.csv", encoding='utf8') as archivo:
        lista_nueva = []
        for line in archivo:
            registro = re.split(",|\n",line)#->Realiza el corte por coma
            diccionario = {}
            diccionario["ID"] = int(registro[0])
            diccionario["Nombre"] = registro[1]
            diccionario["Raza"] = (registro[2].split("-"))
            diccionario["PoderdePelea"] = int(registro[3])
            diccionario["PoderdeDefensa"] = int(registro[4])
            #Explicar Re.sub
            diccionario["Habilidades"] = re.sub(r"[\|\$]","",registro[5]).split("%")
            lista_nueva.append(diccionario)
        return lista_nueva
#2
def ListarCantidadporraza(lista):
    raza_formato = []
    
    for personaje in lista:
        formato = personaje["Raza"][0]
        raza_formato.append(formato)

    lista_raza = raza_formato   
    lista_formato = set(raza_formato)
    
    resultado = []

    for raza in lista_formato:
        contador_raza = 0
        for personaje in lista:
            if personaje["Raza"][0] == raza:
                contador_raza +=1
        resultado.append(f"{raza}: {contador_raza}")
    
    return lista_raza, resultado
#3
def ListarPersonajesporraza(lista):
    #Explicar el set
    lista_formato = ListarCantidadporraza(lista)
    lista_formato = set(lista_formato[0])  
    
    resultado = []
    for razas in lista_formato:
        resultado.append("")
        resultado.append(f"Raza: [{razas}]:")
        for personaje in lista:
            if (razas == (personaje["Raza"][0])):
             resultado.append(f"Nombres: {personaje['Nombre']} | Poder: {personaje['PoderdePelea']}")
    return resultado   
#4  
def ListarPersonajesporHabilidad(lista):
    filtro = input("Ingrese la Habilidad: ")
    resultado = []
    for personaje in lista:
        habilidades = personaje["Habilidades"]
        for habilidad in habilidades:
            if filtro in habilidad:
                nombre = personaje["Nombre"]
                raza = " , ".join(personaje["Raza"])
                promedio = (float(personaje["PoderdePelea"]) + float(personaje["PoderdeDefensa"])) / 2
                resultado.append(f"Nombre: {nombre} - Raza: {raza} - Promedio: {promedio}")
    return resultado
#5
def JugarBatalla(lista):
    personja_Ingresado = input("Ingrese el nombre del personaje: ")
    nombre_jugador = personja_Ingresado
    poder_jugador = 0

    nombre_maquina = ""
    poder_maquina = 0

    resultado = []
    numero_aleatorio = random.randint(1, 10)

    for personaje in lista:
        
        nombres = personaje["Nombre"]
        if personja_Ingresado in nombres:
            nombre_jugador = personja_Ingresado
            poder_jugador = personaje["PoderdePelea"]
            #print(f"Jugador: {nombre_jugador} | Poder: {poder_jugador}")

        id = personaje["ID"]
        if numero_aleatorio == id:
            nombre_maquina = personaje["Nombre"]
            poder_maquina = personaje["PoderdePelea"]
            #print(f"Maquina: {nombre_maquina} | Poder: {poder_maquina}")
    
    if(poder_jugador > poder_maquina):
        resultado.append(f"Gano el jugador.")
        resultado.append(f"Poder: {poder_jugador} Jugador: {nombre_jugador}, Poder Maquina: {poder_maquina} Jugador: {nombre_maquina}")
        ganador = "Jugador"
    else:
        resultado.append(f"Gano la Maquina.")
        resultado.append(f"Poder: {poder_maquina} Jugador: {nombre_maquina}, Poder Jugador: {poder_jugador} Jugador: {nombre_jugador}")
        ganador = "Maquina"

    fecha = datetime.date.today()
    hora_actual = datetime.datetime.now().strftime("%I:%M %p")
    registro = (f"El ganador del juego: '{ganador}', Fecha: {fecha}, Hora: {hora_actual}")
    archivo = open("Registro.txt", "a")
    archivo.write(registro)
    archivo.close()
    return resultado

#6
def GuardarJson(lista):
    global jason_Existe
    resultado = []
    if(jason_Existe == False):
        raza_ingresada = input("Ingrese una raza:")
        habilidad_Ingresada = input("Ingrese una habilidad: ")
        jason_Existe = True
        nombreJason = (f"{raza_ingresada}_{habilidad_Ingresada}")
    else:
        nombreJason = (f"{raza_ingresada}_{habilidad_Ingresada}")

    lista_formato = ListarCantidadporraza(lista)
    concidencias = []
    datos = []
    for personaje in lista_formato:
        raza = personaje
        if raza_ingresada in raza:
            for personaje in lista:
                habilidades = personaje["Habilidades"]
                if (habilidad_Ingresada in habilidades):
                    concidencia = True
                    nombres = personaje["Nombre"]
                    concidencias.append(nombres)

    concidencias = set(concidencias)
    print(concidencias)

    for jugador in lista:
        #Explicar
        habilidades = " + ".join(jugador["Habilidades"])
        if(jugador["Nombre"] in concidencias):
            datos.append({"Datos": f"{jugador['Nombre']} - {jugador['PoderdePelea']} - {habilidades}"})
          
    with open(f"{raza_ingresada}_{habilidad_Ingresada}.json", "a", encoding="utf-8") as file:
        json.dump(datos, file, ensure_ascii=False)
        file.write("\n")

    if(concidencia == True):
        resultado.append(f"Se encontro concidiencia en raza: {raza_ingresada} y habilidad: {habilidad_Ingresada}")
    else:
        resultado.append("No se encontro condicencia")

    return nombreJason,resultado

#7
def LeerJson(lista):
    nombreJason = GuardarJson(lista)
    with open(f"{nombreJason}.json", "r", encoding="utf-8") as j:
        datos = json.load(j)
    # for personaje in datos:
    #     resultado.append(personaje["Datos"])
    return datos


        



