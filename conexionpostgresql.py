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



crear_tabla_query = """

DROP TABLE IF EXISTS  mas1_5, menos1_5, menos2_5, resumen, resumen5dias, signup, tablacapitales, tablariesgos, tabla_datos_hoy;

CREATE TABLE  mas1_5  ( dia_semana  int DEFAULT NULL,  fecha  date DEFAULT NULL, fondo  varchar(150) DEFAULT NULL,  n_1_5  int DEFAULT NULL,  N  int DEFAULT NULL,  n_N   NUMERIC(10,4) DEFAULT NULL);
  

INSERT INTO  mas1_5  ( dia_semana ,  fecha ,  fondo ,  n_1_5 ,  N ,  n_N ) VALUES (1, '2024-09-09', 'BESTIDEAS', 2, 24, 0.0833), (1, '2024-09-09', 'BOLSAESPANA', 6, 31, 0.1935), (1, '2024-09-09', 'BOLSAEUROPA', 6, 57, 0.1053), (1, '2024-09-09', 'BOLSAINTERNACIONAL', 21, 74, 0.2838), (1, '2024-09-09', 'BOLSAUSA', 24, 76, 0.3158), (1, '2024-09-09', 'DIVIDENDO', 8, 42, 0.1905), (1, '2024-09-09', 'FINANCIERO', 18, 34, 0.5294), (1, '2024-09-09', 'GLOBAL', 5, 48, 0.1042), (1, '2024-09-09', 'JAPON', 4, 45, 0.0889), (1, '2024-09-09', 'MEGATRENDS', 12, 37, 0.3243), (1, '2024-09-09', 'NEWENERGY', 8, 37, 0.2162), (1, '2024-09-09', 'SANIDAD', 10, 50, 0.2000), (1, '2024-09-09', 'SECTORINMOBILIARIO', 8, 46, 0.1739), (1, '2024-09-09', 'SMALLCAPS', 18, 67, 0.2687), (1, '2024-09-09', 'TECNOLOGICO', 9, 37, 0.2432), (1, '2024-09-09', 'ZVIX', 0, 0, 0.0000), (1, '2024-09-09', 'ZVSTOXX', 0, 2, 0.0000), (1, '2024-09-09', 'ZVXN', 0, 0, 0.0000);

                              


 

CREATE TABLE  menos1_5  (dia_semana  int DEFAULT NULL, fecha  date DEFAULT NULL, fondo  varchar(150) DEFAULT NULL, n_menos_1_5  int DEFAULT NULL, N  int DEFAULT NULL, n_N   NUMERIC(10,4) DEFAULT NULL);
 

 
 
 

INSERT INTO  menos1_5  ( dia_semana ,  fecha ,  fondo ,  n_menos_1_5 ,  N ,  n_N ) VALUES (1, '2024-09-09', 'BESTIDEAS', 1, 24, 0.0417), (1, '2024-09-09', 'BOLSAESPANA', 1, 31, 0.0323), (1, '2024-09-09', 'BOLSAEUROPA', 1, 57, 0.0175), (1, '2024-09-09', 'BOLSAINTERNACIONAL', 3, 74, 0.0405), (1, '2024-09-09', 'BOLSAUSA', 1, 76, 0.0132), (1, '2024-09-09', 'DIVIDENDO', 2, 42, 0.0476), (1, '2024-09-09', 'FINANCIERO', 1, 34, 0.0294), (1, '2024-09-09', 'GLOBAL', 1, 48, 0.0208), (1, '2024-09-09', 'JAPON', 4, 45, 0.0889), (1, '2024-09-09', 'MEGATRENDS', 1, 37, 0.0270), (1, '2024-09-09', 'NEWENERGY', 10, 37, 0.2703), (1, '2024-09-09', 'SANIDAD', 1, 50, 0.0200), (1, '2024-09-09', 'SECTORINMOBILIARIO', 1, 46, 0.0217), (1, '2024-09-09', 'SMALLCAPS', 4, 67, 0.0597), (1, '2024-09-09', 'TECNOLOGICO', 1, 37, 0.0270), (1, '2024-09-09', 'ZVIX', 1, 0, 0.0000), (1, '2024-09-09', 'ZVSTOXX', 2, 2, 1.0000), (1, '2024-09-09', 'ZVXN', 1, 0, 0.0000);
                              

 

 

CREATE TABLE  menos2_5  (dia_semana  int DEFAULT NULL, fecha  date DEFAULT NULL, fondo  varchar(150) DEFAULT NULL, n_2_5  int DEFAULT NULL, N  int DEFAULT NULL, n_N   NUMERIC(10,4) DEFAULT NULL);

 

 

INSERT INTO  menos2_5  ( dia_semana ,  fecha ,  fondo ,  n_2_5 ,  N ,  n_N ) VALUES (1, '2024-09-09', 'BESTIDEAS', 0, 24, 0.0000), (1, '2024-09-09', 'BOLSAESPANA', 0, 31, 0.0000);

                              

 

 

CREATE TABLE  resumen  ( id  int NOT NULL, fecha  date DEFAULT NULL, dia_semana  int DEFAULT NULL,   fondo  varchar(20) NOT NULL DEFAULT '',   n  int DEFAULT NULL,    peso_porc   NUMERIC DEFAULT NULL,    porc_variacion   NUMERIC DEFAULT NULL,    banco  varchar(50) NOT NULL DEFAULT 'IBERCAJA'); 

 

 

INSERT INTO  resumen  ( id ,  fecha ,  dia_semana ,  fondo ,  n ,  peso_porc ,  porc_variacion ,  banco ) VALUES  (0, '2024-09-13', 5, 'BESTIDEAS', 24, 1, 0.64919, '0.125'), (0, '2024-09-13', 5, 'BOLSAESPANA', 31, 0.9444, 0.99272, '0.484'), (0, '2024-09-13', 5, 'BOLSAEUROPA', 57, 0.8837, 0.59384, '0.158'), (0, '2024-09-13', 5, 'BOLSAINTERNACIONAL', 74, 0.9206, 0.27332, '0.095'),(0, '2024-09-13', 5, 'BOLSAUSA', 76, 0.9523, 0.46998, '0.171');
                              

 
  
 

CREATE TABLE  resumen5dias(  id  int NOT NULL,   fecha  date DEFAULT NULL,   dia_semana  int DEFAULT NULL,   fondo  varchar(20) NOT NULL DEFAULT '',   n  int DEFAULT NULL,   peso_porc   NUMERIC DEFAULT NULL,   porc_variacion   NUMERIC DEFAULT NULL,   banco  varchar(50) NOT NULL);

 
  
 

INSERT INTO  resumen5dias  ( id ,  fecha ,  dia_semana ,  fondo ,  n ,  peso_porc ,  porc_variacion ,  banco ) VALUES (0, '2024-09-09', 1, 'BESTIDEAS', 24, 1, 0.56381, '0.083'),(0, '2024-09-09', 1, 'BOLSAESPANA', 31, 0.9368, 0.74975, '0.194'), (0, '2024-09-09', 1, 'BOLSAEUROPA', 57, 0.9014, 0.33928, '0.105'), (0, '2024-09-09', 1, 'BOLSAINTERNACIONAL', 74, 0.9153, 0.75322, '0.284');
 

CREATE TABLE  signup(id  int NOT NULL, fecha  date DEFAULT NULL, email  varchar(255) DEFAULT NULL, contrasena  varchar(30) DEFAULT NULL,    banco  varchar(50) NOT NULL DEFAULT 'IBERCAJA'); 


 

INSERT INTO  signup  ( id ,  fecha ,  email ,  contrasena ,  banco ) VALUES (0, '2024-02-01', 'b@a.a', '18082470P', 'IBERCAJA'), (0, '2024-02-02', 'a@a.a', '18082470P', 'IBERCAJA');

CREATE TABLE  tablacapitales( id  int NOT NULL, fecha  date DEFAULT NULL, dia_semana  int DEFAULT NULL, fondo  varchar(20) DEFAULT NULL, capital   NUMERIC DEFAULT '0', email  varchar(255) DEFAULT NULL, banco  varchar(50) NOT NULL DEFAULT 'IBERCAJA');

 

INSERT INTO  tablacapitales  ( id ,  fecha ,  dia_semana ,  fondo ,  capital ,  email ,  banco ) VALUES (1, '2022-12-19', 1, 'BOLSAESPANA', 0, 'ff@a.a', 'IBERCAJA'),(2, '2022-12-19', 1, 'BOLSAEUROPA', 0, 'ff@a.a', 'IBERCAJA'), (3, '2022-12-19', 1, 'BOLSAINTERNACIONAL', 0, 'ff@a.a', 'IBERCAJA');

CREATE TABLE  tablariesgos(id  int NOT NULL, fecha  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, fondo  varchar(20) DEFAULT NULL, minima_ganancia   NUMERIC DEFAULT '1', dias_ganancia   NUMERIC DEFAULT '4', dias_perdidas   NUMERIC DEFAULT '5', minima_bajada   NUMERIC DEFAULT '-1.8', maxima_perdida   NUMERIC DEFAULT '5.8', email  varchar(255) DEFAULT NULL, banco  varchar(50) NOT NULL DEFAULT 'IBERCAJA');


 
  
 

INSERT INTO  tablariesgos  ( id ,  fecha ,  fondo ,  minima_ganancia ,  dias_ganancia ,  dias_perdidas ,  minima_bajada ,  maxima_perdida ,  email ,  banco ) VALUES (0, '2024-01-17 16:15:37', 'BESTIDEAS', 1.1, 4, 5, -2.51, -5.77, 'b@a.a', 'IBERCAJA'), (0, '2024-01-17 16:15:37', 'BOLSAESPAÑA', 1.3, 4, 5, -1.92, -4, 'b@a.a', 'IBERCAJA');

CREATE TABLE  tabla_datos_hoy(fecha  date DEFAULT NULL, dia_semana  int DEFAULT NULL, fondo  varchar(20) DEFAULT NULL, Ticker  varchar(15) DEFAULT NULL, accion  varchar(60) DEFAULT NULL, porcentaje   NUMERIC DEFAULT NULL, Modif_porc   NUMERIC DEFAULT NULL, Peso_absoluto   NUMERIC DEFAULT NULL, Precio   NUMERIC DEFAULT NULL, banco  varchar(20) DEFAULT NULL, cnmv  varchar(20) DEFAULT NULL);


"""

cur.execute(crear_tabla_query)

    # Confirmar los cambios
conn.commit()



##cur = conn.cursor()

# Ejecutar una consulta SELECT sobre tablacapitales
cur.execute("SELECT fondo FROM tablacapitales")

# Obtener todos los resultados
rows = cur.fetchall()

# Imprimir los resultados
for row in rows:
    print(row)



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




