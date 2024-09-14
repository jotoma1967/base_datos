#onexion a postgresql

import pip


try:
    import psycopg2

except ImportError:

    pip.main(["install","psycopg2"])

    import psycopg2




import psycopg2

# Datos de conexión
dbname = 'jjtorres18dbname240914'
user = 'jose'
password = 'Gu9VL9h84NYhNB5u3x1wIX9xYy6yL0z8'
host = 'dpg-critv6bv2p9s738on2lg-a'
port = '5432'

# Conexión a la base de datos
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

# Crear un cursor
cur = conn.cursor()

# Ejecutar una consulta
cur.execute("SELECT version();")

# Obtener el resultado
record = cur.fetchone()
print("Conectado a - ", record, "\n")

# Cerrar la conexión
cur.close()
conn.close()

import os

'''
# Ruta relativa del archivo o directorio
ruta_relativa = "mi_archivo.txt"

# Obtener la ruta absoluta
ruta_absoluta = os.path.abspath(ruta_relativa)

print(ruta_absoluta)
'''
import os

# Obtener el directorio actual
directorio_actual = os.getcwd()

print(directorio_actual)




