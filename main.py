from funciones import *

menu = ["--- Dragon Ball ---", "MENU:","1-Listar Cantidad por Raza", "2-Lista Personajes por Raza", "3-Listar Personajes por Habilidad", "4-Jugar Batalla", "5-Guardar Datos en Json", "6-Leer Json", "7-Extra", "8-Salir del programa"]
#
nombreJason = ""
seguir = "si"
jason_Existe = False
jasonCreados = []

for opciones in menu:
    print(opciones)
while seguir == "si":
    respuesta = int(input("Ingrese una opcion: "))
    lista_datos = Traerdatosdesdearchivo()
    match respuesta:
        case 1:
            resultado = ListarCantidadporraza(lista_datos)
            formato = set(resultado)
            for raza in formato:
                contador_raza = 0
                for personaje in lista_datos:
                    if personaje["Raza"][0] == raza:
                        contador_raza +=1
                print(f"{raza}: {contador_raza}")
        case 2:
            resultado = ListarPersonajesporraza(lista_datos)
            for razas in resultado:
                print(razas)
        case 3:
            resultado = ListarPersonajesporHabilidad(lista_datos)
            for habilidad in resultado:
                print(habilidad)
        case 4:
            resultado = JugarBatalla(lista_datos)
            if resultado == None:
                print("No existe el personaje")
            else:
                if (len(resultado) > 0):   
                    for ganador in resultado:
                        print(ganador)
                print("Se genero un archivo TXT")
        case 5:
            resultado = GuardarJson(lista_datos)
            #nombreJason = resultado
            jasonCreados.append(resultado)
            jason_Existe = True
        case 6:
            i = 0
            if(len(jasonCreados) > 0):
                for jsons in jasonCreados:
                    print(f"[{i}]{jsons}")
                    i += 1
            opciones = int(input("Ingrese una opcion: "))
            nombreJason = jasonCreados[opciones]
            resultado = LeerJson(nombreJason)
            for datos in resultado:
                print(datos)
        case 7:
            ejExtra(lista_datos)
        case 8:
            print("Cerrando programa.")
            seguir = "no"
    
    if(seguir == "si"):
        seguir = input("Sigo preguntado?")

    


