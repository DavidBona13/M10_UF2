#Mètodo que et treu per terminal tots els sintetitzadors que hi han dins la base de dades.
def consultar(connection, con_cursor):
    sql = """ SELECT id, nom, marca, tipus, descripcio, connexions FROM public.sintetitzadors"""
    
    con_cursor.execute(sql)
    myresult = con_cursor.fetchall()
    #Recorrer tots els elements de la taula
    for i in myresult:
        print("====================================================================================")
        print("Id: ", i[0])
        print("Nom: ", i[1])
        print("Marca: ", i[2])
        print("Tipus de sintesi: ", i[3])
        print("Descripció: ", i[4])
        print("Tipus de conexions: ", i[5])

#Aquest mètode de consulta serà útil per comprovar en altres mètodes si el sintetitzador ja existeix o no
def consultar2(connection, con_cursor, input1):
    sql = """ SELECT id, nom, marca, tipus, descripcio, connexions FROM public.sintetitzadors WHERE nom = %s"""
    con_cursor.execute(sql, (input1,))
    #En aquest cas s'utilitza el 'fetchone' perquè només volem retornar l'element buscat.
    myresult = con_cursor.fetchone()
    return myresult