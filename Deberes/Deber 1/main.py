#Programa creado por Rafael Vinueza para la materia Python 2020A
import os
import sys

def iniciar_menu():
    print("----------------------------------- Menu Principal -----------------------------------\n")
    print("Digite un numero dependiendo de la operacion que quiera realizar: \n")
    try:   
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
            print("\nLa opcion seleccionada no es correcta.\n")
            iniciar_menu()
    except Exception as error:
            print("\nLa opcion seleccionada no es correcta.\n")
            iniciar_menu()
        
def crear_zoologico():
    nombre_zoologico = input("\nIngrese el nombre del zoologico: ")
    if(os.path.isfile(f"./zoologico_{nombre_zoologico}.txt")):
        print(f"\nEl zoologico '{nombre_zoologico}' ya existe, volvera al menu principal\n")
        iniciar_menu()
    else:
        print("\nIngrese las caracteristicas del zoologico: ")
        try:
            pais_zoologico = input("\nPais del zoologico: ")
            numero_especies_zoologico = int(input("\nNumero de especies: "))
            precio_entrada_zoologico = float(input("\nPrecio de la entrada: "))
            area_zoologico = input("\nArea del zoologico: ")
            hora_apertura_zoologico = input("\nHora de apretura: ")
        except Exception as error:
            print("\nError al leer los datos, regresara al menu principal\n")
            iniciar_menu()

        print("\nIngrese los animales del zoologico: \n")
        try:
            animal1 = input("\nAnimal #1 : ")
            animal2 = input("\nAnimal #2 : ")
            animal3= input("\nAnimal #3 : ")
            animal4 = input("\nAnimal #4 : ")
            animal5 = input("\nAnimal #5 : ")
        except Exception as error:
            print("\nError al leer los datos, regresara al menu principal\n")
            iniciar_menu()

        try:
            file = open(f"./zoologico_{nombre_zoologico}.txt", "w")
            file.write(f"{pais_zoologico};{numero_especies_zoologico};{precio_entrada_zoologico};{area_zoologico};{hora_apertura_zoologico}\n")
            file.write(f"{animal1};{animal2};{animal3};{animal4};{animal5}")
            file.close()
            print(f"\nArchivo 'zoologico_{nombre_zoologico}.txt' creado con exito\n")
            continuar = input("\nPresione enter para regresar al menu principal\n")
            iniciar_menu()
        except Exception as error:
            print("\nError al crear el archivo, regresara al menu principal\n")
            iniciar_menu()

def buscar_zoologico():
    contenido = os.listdir('./')
    contenido.sort
    contenido.remove('main.py')
    if(contenido):
        print("\nEscoja el numero del zoologico para mostrar su informacion: ")
        i = 1
        arreglo_zoologico = []
        for zoologico in contenido:
            zoologico = zoologico.replace("zoologico_","")
            zoologico = zoologico.replace(".txt","")
            arreglo_zoologico.append(zoologico)
            print(f"\n{i} -> {zoologico}")
            i = i + 1
        
        try:
            indice_zoologico = int(input("\neleccion: ")) - 1
        except Exception as error:
            print("\nEl numero ingresado no es correcto, volvera al menu principal.\n")
            iniciar_menu()
        
        archivo_zoologico_abierto = open(f"./zoologico_{arreglo_zoologico[indice_zoologico]}.txt")
        lista_lineas = archivo_zoologico_abierto.readlines()
        archivo_zoologico_abierto.close()
        if(len(lista_lineas) == 2):
            datos_zoologico = lista_lineas[0].split(sep=';')
            datos_animales = lista_lineas[1].split(sep=';')

            print(f"\nLas caracteristicas del zoologico son las siguientes: \n - Pais del zoologico: {datos_zoologico[0]} \n - Numero de especies en el zoologico: {datos_zoologico[1]} \n - Precio de la entrada: {datos_zoologico[2]} \n - Area del zoologico: {datos_zoologico[3]} \n - Hora de apertura del zoologico: {datos_zoologico[4]}")
            print(f"\nLos animales que contiene este zoologico son los siguientes: \n - Animal 1: {datos_animales[0]} \n - Animal 2: {datos_animales[1]} \n - Animal 3: {datos_animales[2]} \n - Animal 4: {datos_animales[3]} \n - Animal 5: {datos_animales[4]} \n")
            continuar = input("\nPresione enter para regresar al menu principal\n")
            iniciar_menu()
        else:
            print("\nEl archivo seleccionado no tiene el formato adecuado. Volvera al menu principal\n")
            iniciar_menu()
            
    else:
        print("\nNo existen archivos de zoologicos, cree uno y regrese. Volvera al menu principal\n")
        iniciar_menu()

def modificar_zoologico():
    contenido = os.listdir('./')
    contenido.sort
    contenido.remove('main.py')
    if(contenido):
        print("\nEscoja el numero del zoologico para modificar su informacion: ")
        i = 1
        arreglo_zoologico = []
        for zoologico in contenido:
            zoologico = zoologico.replace("zoologico_","")
            zoologico = zoologico.replace(".txt","")
            arreglo_zoologico.append(zoologico)
            print(f"\n{i} -> {zoologico}")
            i = i + 1
        
        try:
            indice_zoologico = int(input("\neleccion: ")) - 1
        except Exception as error:
            print("\nEl numero ingresado no es correcto, volvera al menu principal.\n")
            iniciar_menu()
        
        archivo_zoologico_abierto = open(f"./zoologico_{arreglo_zoologico[indice_zoologico]}.txt")
        lista_lineas = archivo_zoologico_abierto.readlines()
        archivo_zoologico_abierto.close()
        if(len(lista_lineas) == 2):
            datos_zoologico = lista_lineas[0].split(sep=';')
            datos_animales = lista_lineas[1].split(sep=';')
            datos_zoologico[4] = datos_zoologico[4].replace("\n", "")
            repetir = 1
            nombre_zoologico_inicial = arreglo_zoologico[indice_zoologico]
            while(repetir == 1):
                print("\nIngrese el numero del dato que desee modificar: \n")
                print(f"1 -> Nombre del zoologico: {arreglo_zoologico[indice_zoologico]}\n2 -> Pais del zoologico: {datos_zoologico[0]} \n3 -> Numero de especies en el zoologico: {datos_zoologico[1]} \n4 -> Precio de la entrada: {datos_zoologico[2]}\n5 -> Area del zoologico: {datos_zoologico[3]}\n6 -> Hora de apertura: {datos_zoologico[4]}\n7 -> Animal 1: {datos_animales[0]} \n8 -> Animal 2: {datos_animales[1]} \n9 -> Animal 3: {datos_animales[2]} \n10 -> Animal 4: {datos_animales[3]} \n11 -> Animal 5: {datos_animales[4]}")
                print(f"12 -> Terminar el proceso de modificacion y guardar")
                eleccion = input("\neleccion: ")

                if(eleccion == "1"):
                    arreglo_zoologico[indice_zoologico] = input("\nIngrese el nuevo nombre del zoologico: ")
                elif(eleccion == "2"):
                    datos_zoologico[0] = input("\nIngrese el nuevo valor del pais del zoologico: ")
                elif(eleccion == "3"):
                    datos_zoologico[1] = input("\nIngrese el nuevo valor del numero de especies en el zoologico: ")
                elif(eleccion == "4"):
                    datos_zoologico[2] = input("\nIngrese el nuevo valor del precio de la entrada: ")
                elif(eleccion == "5"):
                    datos_zoologico[3] = input("\nIngrese el nuevo valor del area del zoologico: ")
                elif(eleccion == "6"):
                    datos_zoologico[4] = input("\nIngrese el nuevo valor de la hora de apertura del zoologico: ")
                elif(eleccion == "7"):
                    datos_animales[0] = input("\nIngrese el nuevo animal 1: ")
                elif(eleccion == "8"):
                    datos_animales[1] = input("\nIngrese el nuevo animal 2: ")
                elif(eleccion == "9"):
                    datos_animales[2] = input("\nIngrese el nuevo animal 3: ")
                elif(eleccion == "10"):
                    datos_animales[3] = input("\nIngrese el nuevo animal 4: ")
                elif(eleccion == "11"):
                    datos_animales[4] = input("\nIngrese el nuevo animal 5: ")
                elif(eleccion == "12"):
                    repetir = 17
                else:
                    print("\nLa opcion seleccionada no es correcta, se termina el proceso de modificacion\n")
                    repetir = 17
            
            os.remove(f"./zoologico_{nombre_zoologico_inicial}.txt")
            file = open(f"./zoologico_{arreglo_zoologico[indice_zoologico]}.txt", "w")
            file.write(f"{datos_zoologico[0]};{datos_zoologico[1]};{datos_zoologico[2]};{datos_zoologico[3]};{datos_zoologico[4]}\n{datos_animales[0]};{datos_animales[1]};{datos_animales[2]};{datos_animales[3]};{datos_animales[4]}")
            file.close()

            continuar = input("\nModificaciones guardadas exitosamente. Presione enter para continuar\n")
            iniciar_menu()
        else:
            print("\nEl archivo seleccionado no tiene el formato adecuado. Volvera al menu principal\n")
            iniciar_menu()

    else:
        print("\nNo existen archivos de zoologicos, cree uno y regrese. Volvera al menu principal\n")
        iniciar_menu()

def eliminar_zoologico():
    contenido = os.listdir('./')
    contenido.sort
    contenido.remove('main.py')
    if(contenido):
        print("\nEscoja el numero del zoologico que desea eliminar: ")
        i = 1
        arreglo_zoologico = []
        for zoologico in contenido:
            zoologico = zoologico.replace("zoologico_","")
            zoologico = zoologico.replace(".txt","")
            arreglo_zoologico.append(zoologico)
            print(f"\n{i} -> {zoologico}")
            i = i + 1
        print(f"\n{i} -> Regresar al menu principal")
        try:
            indice_zoologico = int(input("\neleccion: ")) - 1
        except Exception as error:
            print("\nEl numero ingresado no es correcto, volvera al menu principal.\n")
            iniciar_menu()
        
        if(indice_zoologico + 1 == i):
            iniciar_menu()
        else:
            os.remove(f"./zoologico_{arreglo_zoologico[indice_zoologico]}.txt")
            continuar = input("\nArchivo de zoologico eliminado exitosamente. Presione enter para continuar\n")
            iniciar_menu()
        
    else:
        print("\nNo existen archivos de zoologicos, cree uno y regrese. Volvera al menu principal\n")
        iniciar_menu()


def main():
    iniciar_menu()

if __name__=="__main__":
    main()
