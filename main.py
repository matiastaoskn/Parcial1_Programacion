from funciones import *

jason_Existe = False
seguir = "si"
while seguir == "si":
    respuesta = int(input("Ingrese una opcion: "))
    lista_datos = Traerdatosdesdearchivo()
    match respuesta:
        case 1:
            print("---------")
            print("Elegiste la opcion [1]")
            print("---------")
            resultado = ListarCantidadporraza(lista_datos)
            for raza in resultado[1]:
                print(raza)
            print("---------")
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
            resultado = resultado[1]
            for respuesta in resultado:
                print(respuesta)
            jason_Existe = True
        case 6:
            if(jason_Existe == True):
                resultado = LeerJson(lista_datos)
                print(resultado)
            else:
                print("Necesitas ingresar una habilidad")
    seguir = input("Sigo preguntado?")


