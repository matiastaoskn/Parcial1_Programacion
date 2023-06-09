import re
import random
import datetime
import json
import csv


jason_Existe = False
nombreJason = ""
lista_De_Jasons = []
#0
def Traerdatosdesdearchivo():
    """
    Brief: Generamos una nueva lista mediante una identacion con las claves de un nuevo diccionario
    Parametros: Claves,for,diccionarios
    For:Itera de forma individual por la lista CSV
    return: Retorna una lista con los datos y sus respectivos titulares
    """
    with open("Parcial.csv", encoding='utf8') as archivo:
        lista_nueva = []
        for linea in archivo:
            registro = re.split(",|\n",linea)
            diccionario = {}
            diccionario["ID"] = int(registro[0])
            diccionario["Nombre"] = registro[1]
            diccionario["Raza"] = (registro[2].split("-"))
            diccionario["PoderdePelea"] = int(registro[3])
            diccionario["PoderdeDefensa"] = int(registro[4])
            diccionario["Habilidades"] = re.sub(r"[\|\$]","",registro[5]).split("%")
            lista_nueva.append(diccionario)
        return lista_nueva
#1
def ListarCantidadporraza(lista):
    """
    Brief: Generamos una nueva lista con el clave "Raza" y se mostraran los respectivos contadores de cada una.
    Parametros: Claves,for,diccionarios
    For: Itera en la lista principal y guardar la clave "Raza"
    If: Consulta los valores iterados, si son iguales, se incrementa el contador de esa raza.
    return: Retorna la lista formateada y las razas con sus contadores.
    """
    lista_Raza_Formateada = []
    
    for personaje in lista:
        lista_Raza_Formateada.append(personaje["Raza"][0])
        if(len(personaje["Raza"]) > 1):
            lista_Raza_Formateada.append(personaje["Raza"][1])

    return lista_Raza_Formateada
#2
def ListarPersonajesporraza(lista):
    """
    Brief: Genera los nombres y nivel de poder mediante el titulo de cada "Raza"
    Parametros: Claves,for,diccionarios,if
    For: Itera en una lista obtenida de "Razas" y itera sobre la lista principal, para guardar mas informacion.
    If: Consulta los valores iterados, si son iguales, se guarda el valor de "Nombre y PoderdePelea"
    return: Retorna la lista de todos los valores obtenidos por cada raza.
    """
    lista_Razas_Formateada = ListarCantidadporraza(lista) 
    lista_Razas_Formateada = set(lista_Razas_Formateada)

    resultado = []
    for razas in lista_Razas_Formateada:
        resultado.append("")
        resultado.append(f"Raza: [{razas}]:")
        for personaje in lista:
            if (razas == (personaje["Raza"][0])):
                resultado.append(f"Nombres: {personaje['Nombre']} | Poder: {personaje['PoderdePelea']}")
    return resultado
#3 
def ListarPersonajesporHabilidad(lista):
    """
    Brief: Genera los nombres y promedio de poder, defensa mediante un filtro que el usuario brinda de "Habilidad".
    Parametros: Claves,for,diccionarios,if
    For: Itera en la lista principal y el filtro brindando, buscando la indentidad.
    If: Consulta los valores iterados, si son iguales, se guarda el valor de "Nombre y Promedio de Ataque y defensa"
    return: Retorna la lista de todos los valores obtenidos por cada raza.
    """
    for habilidades in lista:
        print(habilidades["Habilidades"])

    valor_Ingresado_filtro = input("Ingrese la Habilidad: ")
    
    resultado = []
    for personaje in lista:
        habilidades = personaje["Habilidades"]
        for habilidad in habilidades:
            if valor_Ingresado_filtro in habilidad:
                nombre = personaje["Nombre"]
                raza = " , ".join(personaje["Raza"])
                promedio = (float(personaje["PoderdePelea"]) + float(personaje["PoderdeDefensa"])) / 2
                resultado.append(f"Nombre: {nombre} - Raza: {raza} - Promedio: {promedio}")
    return resultado
#4
def JugarBatalla(lista):
    """
    Brief: Se ingresa un nombre y mediante un numero random se genera el jugador de la maquina.
    El jugador con mas poder gana, guardando informacion en .TXT
    For: Itera en la lista principal
    If: Consulta si el poder del jugador o de la maquina es mas grande que el otro.
    return: Retorna indicaciones sencillas para el usuario sobre el archivo TXT
    """
    i = 0
    lista_Nombres = []
    for personaje in lista:
        print(f"[{i}]-{personaje['Nombre']}")
        i += 1
        lista_Nombres.append(personaje['Nombre'])

    personja_Ingresado = input("Ingrese el nombre del personaje: ")
    while(personja_Ingresado not in lista_Nombres):
        personja_Ingresado = input("Ingreso un valor Invalido. Ingrese el nombre del personaje: ")
    
    for personajes in lista:
        if personja_Ingresado == personajes["Nombre"]:
            nombre_jugador = personja_Ingresado
            poder_jugador = 0    

            nombre_maquina = ""
            poder_maquina = 0

            resultado = []
            numero_aleatorio = random.randint(1, 10)

            for personaje in lista:
                
                nombres = personaje["Nombre"]
                if personja_Ingresado == nombres:
                    nombre_jugador = personja_Ingresado
                    poder_jugador = personaje["PoderdePelea"]
                    

                id = personaje["ID"]
                if numero_aleatorio == id:
                    nombre_maquina = personaje["Nombre"]
                    poder_maquina = personaje["PoderdePelea"]
                    
            
            if(poder_jugador > poder_maquina):
                ganador = "Jugador"
                ganador_Nombre = nombre_jugador
                perdedor_Nombre = nombre_maquina
            else:
                ganador = "Maquina"
                ganador_Nombre = nombre_maquina
                perdedor_Nombre = nombre_jugador

            fecha = datetime.date.today()
            hora_actual = datetime.datetime.now().strftime("%I:%M %p")
            registro = (f"El ganador del juego: '{ganador}', Nombre: {ganador_Nombre}, Perdedor: {perdedor_Nombre} Fecha: {fecha}, Hora: {hora_actual}\n")
            archivo = open("Registro.txt", "a")
            archivo.write(registro)
            archivo.close()
            return resultado
#5
def GuardarJson(lista):
    """
    Brief: Mediante dos filtros, se busca la similitud en los demas personajes. Se guardan esas busquedas con sus valores.
    En un formato .JSON
    For: Itera en la lista de "Raza" y en la lista principal.
    If: Consulta la identidad de "Razas" y la identidad de sus habilidades con las encontradas mediante el primer IF
    return: Retorna el nombre del archivo.json y retorna una indicacion simple para el usuario.
    """
    
    lista_razas = ListarCantidadporraza(lista)
    lista_razas = set(lista_razas)
    i = 0
    
    for razas in lista_razas:
        print(f"[{i}]-Raza:{razas}")
        i += 1

    lista_Formato_Habilidades = []

    #Validacion de Raza y lista de Razas
    raza_ingresada = input("Ingrese una raza:")
    while(raza_ingresada not in lista_razas):
        raza_ingresada = input("Ingreso una raza invalida. Ingrese una raza:")
    
    #Validacion y lista de Habilidades
    for habilidad in lista:
        lista_Habilidades = habilidad["Habilidades"]
        for habilidad in lista_Habilidades:
            print(f"[{i}]-Habilidades:{habilidad}")

   #Formato para la lista de habilidades y facilidad para el usuario.
    habilidad_Ingresada = input("Ingrese una habilidad: ")
    for personaje in lista:
        for habilidad in personaje["Habilidades"]:
            lista_Formato_Habilidades.append(habilidad.replace(" ", "").lower())
    while(habilidad_Ingresada not in lista_Formato_Habilidades):
        habilidad_Ingresada = input("Ingreso una habilidad invalida. Ingrese una habilidad: ")

    nombreDelJason = (f"{raza_ingresada}_{habilidad_Ingresada}")
    lista_De_Jasons.append(nombreDelJason)

    for personaje in lista:
            nombreJason = (f"{raza_ingresada}_{habilidad_Ingresada}")
            lista_Raza_Formateada = ListarCantidadporraza(lista)

            concidencias = []
            datos = []

            for razas in lista_Raza_Formateada:
                raza = razas
                if raza_ingresada in raza:
                    for personaje in lista:
                        habilidades = personaje["Habilidades"]
                        if (habilidad_Ingresada in habilidades):
                            nombres = personaje["Nombre"]
                            concidencias.append(nombres)

            concidencias = set(concidencias)  

            for jugador in lista:
                habilidades = " + ".join(jugador["Habilidades"])
                if(jugador["Nombre"] in concidencias):
                    datos.append({"Datos": f"{jugador['Nombre']} - {jugador['PoderdePelea']} - {habilidades}\n"})
            with open(f"{nombreDelJason}.json", "a", encoding="utf-8") as file:
                json.dump(datos, file, ensure_ascii=False)
                file.write("\n")

                
            return nombreJason
#6
def LeerJson(nombre):
    """
    Brief: Mediante un parametro, lee el archivo que se le indique y se obtienen esos datos para despues imprimirlos.
    return: Retorna el valor de la lectura del archivo.
    """
    with open(f"{nombre}.json", "r", encoding="utf-8") as j:
        datos = json.load(j)
    return datos
#7
def ejExtra(lista):
    with open("nuevo.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        filtro = "Saiyan"
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

