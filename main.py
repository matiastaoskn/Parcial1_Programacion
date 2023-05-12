from funciones import *

menu = ["--- Dragon Ball ---", "MENU:","1-Listar Cantidad por Raza", "2-Lista Personajes por Raza", "3-Listar Personajes por Habilidad", "4-Jugar Batalla", "5-Guardar Datos en Json", "6-Leer Json", "7-Salir"]
#
nombreJason = ""
seguir = "si"
for opciones in menu:
    print(opciones)
while seguir == "si":
    respuesta = int(input("Ingrese una opcion: "))
    lista_datos = Traerdatosdesdearchivo()
    match respuesta:
        case 1:
            resultado = ListarCantidadporraza(lista_datos)
            for raza in resultado[1]:
                print(raza)
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
            for ganador in resultado:
                print(ganador)
        case 5:
            resultado = GuardarJson(lista_datos)
            print(resultado[0])
            nombreJason = resultado[1]
            jason_Existe = True
        case 6:
            if(jason_Existe == True):
                resultado = LeerJson(nombreJason)
                for datos in resultado:
                    print(datos["Datos"])
            else:
                print("Debe ingresar una Raza y una habilidad [Opcion: 5]")
        case 7:
            print("Cerrando programa.")
            seguir = "no"
    
    if(seguir == "si"):
        seguir = input("Sigo preguntado?")
    


