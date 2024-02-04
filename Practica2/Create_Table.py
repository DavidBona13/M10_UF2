#Creació de la taula sintetitzador, si es fa la comprovació, diu que ja existeix. Li pasem la conexió i el cursor.
def crearTaula(connection, con_cursor):
    sql = """CREATE TABLE SINTETITZADORS(
                id SERIAL PRIMARY KEY,
                nom VARCHAR(30) NOT NULL,
                marca VARCHAR(30) NOT NULL,
                tipus VARCHAR(55) NOT NULL,
                descripcio VARCHAR(255) NOT NULL,
                connexions VARCHAR(255) NOT NULL           
    )
    """
    con_cursor.execute(sql)
    connection.commit()
    