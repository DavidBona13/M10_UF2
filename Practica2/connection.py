import psycopg2

def connexio():
    conn = psycopg2.connect(
        database="postgres",
        user='david_postgres',
        password='battlefield2042_postgres',
        host='localhost',
        port='5432'
    )

    #connection = conn.cursor()
    return conn
