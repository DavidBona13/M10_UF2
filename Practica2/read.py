def consultar(connection, con_cursor):
    sql = """ SELECT id, nom, marca, tipus, descripcio, connexions FROM public.sintetitzadors"""
    
    con_cursor.execute(sql)
    myresult = con_cursor.fetchall()
    
    for i in myresult:
        print("====================================================================================")
        print("Id: ", i[0])
        print("Nom: ", i[1])
        print("Marca: ", i[2])
        print("Tipus de sintesi: ", i[3])
        print("Descripció: ", i[4])
        print("Tipus de conexions: ", i[5])

def consultar2(connection, con_cursor, input1):
    sql = """ SELECT id, nom, marca, tipus, descripcio, connexions FROM public.sintetitzadors WHERE nom = %s"""
    con_cursor.execute(sql, (input1,))
    myresult = con_cursor.fetchone()
    return myresult