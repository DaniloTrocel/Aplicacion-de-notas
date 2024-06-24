import os
from tabulate import tabulate
from conexion import *
from nota import Nota

con = conectar()

def iniciar():
    print('Bienvenido al sistema de notas')
    print('1. Ingresar notas')
    print('2. Ver notas')
    print('3. Ver contenido')
    print('4. Modificar nota')
    print('5. Eliminar nota')
    print('6. Salir')
    while True:
        opcion = input('Ingrese una opción: ')
        if opcion == '1':
            nueva_nota()
        elif opcion == '2':
            ver_notas()
        elif opcion == '3':
            ver_contenido()
        elif opcion == '4':
            modificar_nota()
        elif opcion == '5':
            eliminar_nota()
        elif opcion == '6':
            print('Hasta luego')
            break
        else:
            print('Opción incorrecta')
        


def nueva_nota():
    nombre = input('Ingrese el nombre de la nota: ')
    contenido = input('Ingrese el contenido de la nota: ')
    nota = Nota(nombre=nombre, contenido=contenido)
    respuesta = nota.registrar()
    print(respuesta)


def ver_notas():
    nota = Nota()
    datos = nota.mostrar()
    headers = ['ID', 'Nombre', 'Fecha de creación']
    tabla = tabulate(datos, headers, tablefmt='fancy_grid')
    print(tabla)


        
def ver_contenido():
      id = input('Ingrese el ID de la nota: ')
      nota = Nota(id=id)
      resultado = nota.buscar()
      if len(resultado):
          file = open(f'./notas/{resultado[0][1]}', 'r')
          print('\n'+file.read()+'\n')
          file.close()
      else:
            print('La nota no existe')  

def modificar_nota():
    archivos = os.listdir('./notas')
    for numero, archivo in enumerate(archivos):
        print(f'{numero+1} {archivo}') 
    seleccionado = int(input('Seleccione el archivo a modificar: ')) - 1
    nuevo_contenido = input('\nIngrese el nuevo contenido: ')
    file = open(f'./notas/{archivos[seleccionado]}', 'w') 
    file.write(nuevo_contenido)
    file.close()
    print('Nota modificada correctamente')   


def eliminar_nota():
    id = input('Ingrese el ID de la nota que desea borrar: ')
    nota = Nota(id=id)
    resultado = nota.eliminar()
    print(resultado)

iniciar()    