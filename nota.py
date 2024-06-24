from conexion import *
from datetime import date

class Nota:
    def __init__(self, id='', nombre='', contenido=''):
        self.id = id
        self.nombre = f'{nombre}.txt'
        self.contenido = contenido
        self.fecha_creacion = date.today()

    def registrar(self):
        try:
            con = conectar()
            cursor = con.cursor()
            sql = 'INSERT INTO nota (nombre, fecha_creacion) VALUES(%s, %s)'
            datos = (self.nombre, self.fecha_creacion)
            cursor.execute(sql, datos)
            self.crear_nota()
            con.commit()
            con.close()
            print('Nota registrada correctamente')
        except mysql.Error as err:
            print('Ha ocurrido un error al registrar la nota', err)    

    def crear_nota(self):
        try:
            file = open(f'./notas/{self.nombre}', 'w')
            file.write(self.contenido)
            file.close()
        except OSError as err:
            print('Ha ocurrido un error al crear la nota', err)           

    def mostrar(self):
        datos = []
        try:
            con = conectar()
            cursor = con.cursor()
            sql = 'SELECT * FROM nota'
            cursor.execute(sql)
            datos = cursor.fetchall()
            con.close()
        except mysql.Error as err:  
            print('Ha ocurrido un error al mostrar las notas', err)
        return datos      

    def buscar(self):
        datos = []
        try:
            con = conectar()
            cursor = con.cursor()
            sql = f'SELECT * FROM nota WHERE id={self.id}'
            cursor.execute(sql)
            datos = cursor.fetchall()
            con.close()
        except mysql.Error as err:  
            print('Ha ocurrido un error al buscar la nota', err)
        return datos       
    
    def eliminar(self):
        try:
            con = conectar()
            cursor = con.cursor()
            sql = f'DELETE FROM nota WHERE id={self.id}'
            cursor.execute(sql)
            con.commit()
            con.close()
            return 'Se ha eliminado correctamente'
        except mysql.Error as err:  
            print('Ha ocurrido un error al eliminar la nota', err)  