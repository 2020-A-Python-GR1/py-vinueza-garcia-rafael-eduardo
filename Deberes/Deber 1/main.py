#Programa creado por Rafael Vinueza para la materia Python 2020A
import os
import sys

def iniciar_menu():
    print("----------------------------------- Menu Principal -----------------------------------\n")
    print("Digite un numero dependiendo de la operacion que quiera realizar: \n")
    opcion_zoologico = input(" 1 -> Crear Zoologico \n 2 -> Leer los datos de un Zoologico \n 3 -> Modificar Zoologico \n 4 -> Eliminar Zoologico (incluyendo sus animales) \n 5 -> Salir del programa \n\n eleccion: ")

    if(opcion_zoologico == "1"):
        crear_zoologico()
    elif(opcion_zoologico == "2"):
        buscar_zoologico()
    elif(opcion_zoologico == "3"):
        modificar_zoologico()
    elif(opcion_zoologico == "4"):
        eliminar_zoologico()
    elif(opcion_zoologico == "5"):
        sys.exit()
    else:
        print("La opcion seleccionada no es correcta.\n")
        iniciar_menu()
        



def crear_zoologico():
    nombre_zoologico = input("\nIngrese el nombre del zoologico: ")
    if(os.path.isfile(f"./zoologico_{nombre_zoologico}.txt")):
        print(f"El zoologico '{nombre_zoologico}' ya existe, volvera al menu principal\n")
        iniciar_menu()
    else:
        print("Ingrese las caracteristicas del zoologico: \n")
        try:
            pais_zoologico = input("\nPais del zoologico: ")
            numero_especies_zoologico = input("\nNumero de especies: ")
            precio_entrada_zoologico = input("\nPrecio de la entrada: ")
            area_zoologico = input("\nArea del zoologico: ")
            hora_apertura_zoologico = input("\nHora de apretura: ")
        except error:
            print("Error al leer los datos, regresara al menu principal")
            iniciar_menu()

        try:
            file = open(f"./zoologico_{nombre_zoologico}.txt", "w")
            file.write(f"{pais_zoologico};{numero_especies_zoologico};{precio_entrada_zoologico};{area_zoologico};{hora_apertura_zoologico}")
            file.close()
            print(f"Archivo 'zoologico_{nombre_zoologico}.txt' creado con exito")
            iniciar_menu()
        except error:
            print("Error al crear el archivo, regresara al menu principal")
            iniciar_menu()

            
def main():
    iniciar_menu()

if __name__=="__main__":
    main()
