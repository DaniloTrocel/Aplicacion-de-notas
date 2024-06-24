import mysql.connector as mysql

def conectar():
    try:
        conexion = mysql.connect(
            host='localhost',
            user = 'root',
            passwd = '',
            database = 'notas'
        )
        print('Se ha conectado a la base de datos')
        return conexion
    except mysql.Error as err:
        print('Ha ocurrido un error al conectarse', err)