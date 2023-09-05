import libro as l

# Crear una lista vacía para almacenar los libros
libros =[]

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)
libros.append(l.nuevo_libro)

def ejemplares_prestados():
    # completar
    return None

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    codigo = str(len(libros) + 1) #manera de codigo automatico
    Ejemplares = int(input("Ingrese la cantidad de ejemplares del libro\n"))
    titulo = input("Ingrese el titulo del libro\n")
    autor = input("Ingrese el nombre del autor\n")

    print("Libro agregado correctamente!")

    
    return None

def eliminar_ejemplar_libro():
    
    return None

"""def prestar_ejemplar_libro():
    
    return None"""

def devolver_ejemplar_libro():
    respuesta = input("Desea devolver un libro?")

    while respuesta == "si":
     cod= input("Ingrese el codigo del libro: ")

    if cod == 'CRBJsAkS':
        print(f"{libro1} este libro posee tres ejemplar")

    elif cod == 'QgfV4j3c':
        print(f"{libro2} este libro posee cuatro ejemplares")
        
    elif cod == 'adOd09UE':
        print(f"{libro3} Este libro un ejemplar")

    else:
        print("Error.Codigo invalido")

    print("Devolución realizada")
     
    #Falta mostrar la cantidades de ejemplares

    return None

"""def nuevo_libro():
    #completar
    return None"""

import random
import string

# get random password pf length 8 with letters, digits, and symbols
def generar():
    characters = string.ascii_letters + string.digits
    cod = ''.join(random.choice(characters) for i in range(8))
    return cod

libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

EjemplaresLibro1 = 1
EjemplaresLibro2 = 2
EjemplaresLibro3 = 0


def generar_codigo():
    cod= input("Ingrese el codigo del libro: ")

    if cod == 'CRBJsAkS':
        print(libro1)

    elif cod == 'QgfV4j3c':
        print(libro2)
        
    elif cod == 'adOd09UE':
        print(libro3)

    else:
        print("Error.Codigo invalido")
    return None


import os

print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Gestionar Prestamo")
    print("2 - Gestionar Devolucion")
    print("3 - Registrar nuevo libro")
    print("4 - Elimiar ejemplar")
    print("5 - Mostrar ejemplares perstados")
    print("6 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            generar_codigo()
        elif int(opt) == 2:
            #completar
            print()
        elif int(opt) == 3:
            registrar_nuevo_libro()
            
        elif int(opt) == 4:
            #completar
            print()
        elif int(opt) == 5:
            #completar
            print()
        elif int(opt) == 6:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....") # Pausa

print("Hasta luego!.")





