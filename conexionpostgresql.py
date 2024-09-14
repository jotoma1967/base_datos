#onexion a postgresql
import psycopg2

# Datos de conexión
dbname = 'jjtorres18dbname240914'
user = 'jose'
password = 'Gu9VL9h84NYhNB5u3x1wIX9xYy6yL0z8'
host = 'postgresql://jose:Gu9VL9h84NYhNB5u3x1wIX9xYy6yL0z8@dpg-critv6bv2p9s738on2lg-a.oregon-postgres.render.com/jjtorres18dbname240914'
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
