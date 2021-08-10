import pandas as pd
import sqlite3
import numpy as np

# Leyendo archivo .CSV
def LecturaBD():
    try:
        BaseDatos = pd.read_csv('bdatos.csv', index_col=None)
        return BaseDatos
    except TypeError:
        print("Archivo CSV no encontrado\n")
    except UnboundLocalError:
        print("Archivo CSV no encontrado\n")
    except FileNotFoundError as FileNot:
        print(f"Archivo CSV no encontrado {FileNot}\n")

# Creando conexión con la BD
def ConexionBD():
    try:
        Conexion = sqlite3.connect("Registro.db")
        return Conexion
    except sqlite3.error as Error:
        print(f"Error al crear la conexión con la base de datos{Error}")

# Creando tabla para Registro de usuarios
def TablaUsuarios(Conexion):
    Cursor = Conexion.cursor()
    Cursor.execute("CREATE TABLE IF NOT EXISTS Usuarios( IDENTIFICACION INTEGER(20),"
                   "TIPO_IDENTIFICACION VARCHAR (10),"
                   "PRIMER_NOMBRE VARCHAR (20),"
                   "SEGUNDO_NOMBRE VARCHAR (20),"
                   "PRIMER_APELLIDO VARCHAR (20),"
                   "SEGUNDO_APELLIDO VARCHAR (20),"
                   "DIRECCION VARCHAR (20),"
                   "CELULAR INTEGER(15),"
                   "CIUDAD VARCHAR(30),"
                   "SALARIO FLOAT(30) )")
    Conexion.commit()

# Registrando todos los usuarios del archivo .CSV
def RegistroUsuarios(Conexion, BD):
    BD = np.array(BD)
    BD = tuple(BD)
    Cursor = Conexion.cursor()
    Cursor.executemany(
        "INSERT INTO Usuarios ('IDENTIFICACION','TIPO_IDENTIFICACION','PRIMER_NOMBRE','SEGUNDO_NOMBRE','PRIMER_APELLIDO',"
        "'SEGUNDO_APELLIDO','DIRECCION','CELULAR','CIUDAD','SALARIO') VALUES (?,?,?,?,?,?,?,"
        "?,?,?)", BD)
    Conexion.commit()

# Extrayendo usuarios que viven en MANIZALES, PEREIRA y las restantes
def Ciudades(BD):
    Manizales = BD[BD["CIUDAD"] == "MANIZALES"]
    Pereira = BD[BD["CIUDAD"] == "PEREIRA"]
    OtrasCiudades = BD[(BD["CIUDAD"] != "MANIZALES") & (BD["CIUDAD"] != "PEREIRA")]
    return Manizales, Pereira, OtrasCiudades

# Creando tabla para usuarios que viven en Manizales
def TablaManizales(Conexion):
    Cursor = Conexion.cursor()
    Cursor.execute("CREATE TABLE IF NOT EXISTS CiudadManizales( IDENTIFICACION INTEGER(20),"
                   "TIPO_IDENTIFICACION VARCHAR (10),"
                   "PRIMER_NOMBRE VARCHAR (20),"
                   "SEGUNDO_NOMBRE VARCHAR (20),"
                   "PRIMER_APELLIDO VARCHAR (20),"
                   "SEGUNDO_APELLIDO VARCHAR (20),"
                   "DIRECCION VARCHAR (20),"
                   "CELULAR INTEGER(15),"
                   "CIUDAD VARCHAR(30),"
                   "SALARIO FLOAT(30) )")
    Conexion.commit()

# Registro para usuarios que viven en Manizales
def RegistroManizales(Conexion, Manizales):
    Manizales = np.array(Manizales)
    Manizales = tuple(Manizales)
    Cursor = Conexion.cursor()
    Cursor.executemany(
        "INSERT INTO CiudadManizales ('IDENTIFICACION','TIPO_IDENTIFICACION','PRIMER_NOMBRE','SEGUNDO_NOMBRE','PRIMER_APELLIDO',"
        "'SEGUNDO_APELLIDO','DIRECCION','CELULAR','CIUDAD','SALARIO') VALUES (?,?,?,?,?,?,?,"
        "?,?,?)", Manizales)
    Conexion.commit()

# Creando tabla para usuarios que viven en Pereira
def TablaPereira(Conexion):
    Cursor = Conexion.cursor()
    Cursor.execute("CREATE TABLE IF NOT EXISTS CiudadPereira( IDENTIFICACION INTEGER(20),"
                   "TIPO_IDENTIFICACION VARCHAR (10),"
                   "PRIMER_NOMBRE VARCHAR (20),"
                   "SEGUNDO_NOMBRE VARCHAR (20),"
                   "PRIMER_APELLIDO VARCHAR (20),"
                   "SEGUNDO_APELLIDO VARCHAR (20),"
                   "DIRECCION VARCHAR (20),"
                   "CELULAR INTEGER(15),"
                   "CIUDAD VARCHAR(30),"
                   "SALARIO FLOAT(30) )")
    Conexion.commit()

# Registro para usuarios que viven en Pereira
def RegistroPereira(Conexion, Pereira):
    Pereira = np.array(Pereira)
    Pereira = tuple(Pereira)
    Cursor = Conexion.cursor()
    Cursor.executemany(
        "INSERT INTO CiudadPereira ('IDENTIFICACION','TIPO_IDENTIFICACION','PRIMER_NOMBRE','SEGUNDO_NOMBRE','PRIMER_APELLIDO',"
        "'SEGUNDO_APELLIDO','DIRECCION','CELULAR','CIUDAD','SALARIO') VALUES (?,?,?,?,?,?,?,"
        "?,?,?)", Pereira)
    Conexion.commit()

# Creando tabla para usuarios que viven en otras ciudades
def TablaOtrasCiudades(Conexion):
    Cursor = Conexion.cursor()
    Cursor.execute("CREATE TABLE IF NOT EXISTS OtrasCiudades( IDENTIFICACION INTEGER(20),"
                   "TIPO_IDENTIFICACION VARCHAR (10),"
                   "PRIMER_NOMBRE VARCHAR (20),"
                   "SEGUNDO_NOMBRE VARCHAR (20),"
                   "PRIMER_APELLIDO VARCHAR (20),"
                   "SEGUNDO_APELLIDO VARCHAR (20),"
                   "DIRECCION VARCHAR (20),"
                   "CELULAR INTEGER(15),"
                   "CIUDAD VARCHAR(30),"
                   "SALARIO FLOAT(30) )")
    Conexion.commit()

# Registro para usuarios que viven en otras ciudades
def RegistroOtrasCiudades(Conexion, Otras_Ciudades):
    Otras_Ciudades = np.array(Otras_Ciudades)
    Otras_Ciudades = tuple(Otras_Ciudades)
    Cursor = Conexion.cursor()
    Cursor.executemany(
        "INSERT INTO OtrasCiudades ('IDENTIFICACION','TIPO_IDENTIFICACION','PRIMER_NOMBRE','SEGUNDO_NOMBRE','PRIMER_APELLIDO',"
        "'SEGUNDO_APELLIDO','DIRECCION','CELULAR','CIUDAD','SALARIO') VALUES (?,?,?,?,?,?,?,"
        "?,?,?)", Otras_Ciudades)
    Conexion.commit()

if __name__ == '__main__':
    try:
        BD = LecturaBD()  # Leyendo archivo CSV
        Conexion = ConexionBD()  # Creando conexión con la base datos
        TablaUsuarios(Conexion)  # Creando tabla (Vacía) para el registro completo de los datos del archivos CSV
        RegistroUsuarios(Conexion, BD)  # Registrando todos los usuarios en la tabla principal.
        Manizales, Pereira, OtrasCiudades = Ciudades(BD)  # Registrando todos los usuarios que viven en manizales
        TablaManizales(Conexion) # Creando tabla (Vacía) para el registro de personas que viven en Manizales
        RegistroManizales(Conexion, Manizales) # Registrando todos los usuarios que viven en Manizales
        TablaPereira(Conexion) # Creando tabla (Vacía) para el registro de personas que viven en Pereira
        RegistroPereira(Conexion, Pereira) # Registrando todos los usuarios que viven en Pereira
        TablaOtrasCiudades(Conexion) # Creando tabla (Vacía) para el registro de personas que viven en otras ciudades
        RegistroOtrasCiudades(Conexion, OtrasCiudades) # Registrando todos los usuarios que viven en otras ciudades
        if Conexion:
            Conexion.close()
    except TypeError as Error:
        print("La base de datos no ha sido cargada correctamente", Error)
