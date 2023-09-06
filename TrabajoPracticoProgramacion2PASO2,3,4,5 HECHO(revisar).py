import libro as l

# Crear una lista vacía para almacenar los libros
libros =[libro1, libro2, libro3]

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)
libros.append(l.nuevo_libro)

libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

EjemplaresLibro1 = 3
EjemplaresLibro2 = 4
EjemplaresLibro3 = 1

#1 
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

#2
def devolver_ejemplar_libro():
    respuesta = input("Desea devolver un libro? (si o no)")

    while respuesta == "si":
     cod= input("Ingrese el codigo del libro: ")

    if cod == 'CRBJsAkS':
        print(f"{libro1} este libro posee {EjemplaresLibro1} ejemplares")

    elif cod == 'QgfV4j3c':
        print(f"{libro2} este libro posee {EjemplaresLibro2} ejemplares")
        
    elif cod == 'adOd09UE':
        print(f"{libro3} Este libro posee {EjemplaresLibro3} ejemplar")

    else:
        print("Error.Codigo invalido")

    print("Devolución realizada")
     
    #Falta mostrar la cantidades de ejemplares

    return None

#3
def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    codigo = str(len(libros) + 1) #manera de codigo automatico
    Ejemplares = int(input("Ingrese la cantidad de ejemplares del libro\n"))
    titulo = input("Ingrese el titulo del libro\n")
    autor = input("Ingrese el nombre del autor\n")

    print("Libro agregado correctamente!")

    
    return None


#4
def eliminar_ejemplar_libro():
    cod= input("Ingrese el codigo del libro: ")

    if cod == 'CRBJsAkS':
        print(libro1)
        BorrarLibro1 = EjemplaresLibro1 - 4
        print("El libro ha sido eliminado.")
    elif cod == 'QgfV4j3c':
        print(libro2)
        BorrarLibro2 = EjemplaresLibro2 - 3
        print("El libro ha sido eliminado.")
    elif cod == 'adOd09UE':
        print(libro3)
        BorrarLibro3 = EjemplaresLibro3 - 1
        print("El libro ha sido eliminado.")
    else:
        print("Error.Codigo invalido")
    

    """if libro['cod'] == codigo:
            if libro['cant_ej_ad'] > 0:
                libro['cant_ej_ad'] -= 1
                print(f"Se ha eliminado un ejemplar de '{libro['titulo']}'")
            else:
                print(f"No hay ejemplares disponibles para eliminar de '{libro['titulo']}'")
            return
    print("Error: El código ingresado no corresponde a ningún libro.")
"""

    return None


#5
def ejemplares_prestados():
    if libros['cant_ej_pr'] > 0:
        print(f"Libro: {libros['titulo']}, Ejemplares prestados: {libros['cant_ej_pr']}")
    else:
        print(f"No hay ejemplares prestados de {libros['titulo']}")
    return None



"""def prestar_ejemplar_libro():
    
    return None"""



"""def nuevo_libro():
    #completar
    return None"""

import random
import string

# get random password pf length 8 with letters, digits, and symbols
"""def generar():
    characters = string.ascii_letters + string.digits
    cod = ''.join(random.choice(characters) for i in range(8))
    return cod"""







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
            devolver_ejemplar_libro()
            print()
        elif int(opt) == 3:
            registrar_nuevo_libro()
            
        elif int(opt) == 4:
            eliminar_ejemplar_libro()
            
        elif int(opt) == 5:
            ejemplares_prestados()
            
        elif int(opt) == 6:
            respuesta = "salir"
            print("Usted ha salido del programa")
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....") # Pausa

print("Hasta luego!.")




