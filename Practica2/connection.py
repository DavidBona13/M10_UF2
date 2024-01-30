import psycopg2

conn = psycopg2.connect(
    database="postgres",
    user='david_postgres',
    password='battlefield2042_postgres',
    host='localhost',
    port='5432'
)

connection = conn.cursor()

print(connection)