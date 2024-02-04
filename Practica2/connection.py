import psycopg2

#Connexió base de dades PostgreSQL
def connexio():
    conn = psycopg2.connect(
        database="postgres",
        user='david_postgres',
        password='battlefield2042_postgres',
        host='localhost',
        port='5432'
    )
    #Retornem el conn, el cursor el crearem a la classe main. 
    return conn
