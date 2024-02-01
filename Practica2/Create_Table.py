import psycopg2
def crear(connection):
    conn = connection.cursor()
    sql = """CREATE TABLE SINTETITZADORS(
                id SERIAL PRIMARY KEY,
                nom VARCHAR(30) NOT NULL,
                marca VARCHAR(30) NOT NULL,
                tipus VARCHAR(55) NOT NULL,
                descripcio VARCHAR(255) NOT NULL,
                connexions VARCHAR(255) NOT NULL           
    )
    """
    conn.execute(sql)
    connection.commit()
    conn.close()
    