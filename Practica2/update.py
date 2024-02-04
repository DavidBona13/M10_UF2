from read import consultar2

def modificar(connection, con_cursor):
    a = True
    while a:
        #Comprovació de si el sintetitzador existeix o no
        input1 = input("Si us plau, introdueix-hi el nom del sintetitzador que vols modificar ")
        vari1 = consultar2(connection, con_cursor, input1)
        
        if vari1:
            input2 = input("Si us plau, introdueix-hi la nova descripció ")
            sql = """ UPDATE public.sintetitzadors SET descripcio = %s WHERE nom = %s
            """
            con_cursor.execute(sql, (input2, input1))
            connection.commit()
            
            print("Sintetitzador modificat correctament!\n ")
            #El que fem a qui és cridar el mètode consultar2 perquè et busqui dins la base de dades la modificació feta i la tregui per pantalla perquè la puguis veure.
            vari2 = consultar2(connection, con_cursor, input1)
            print(vari2)
            #Sortir del bucle
            a = False
        else:
            print("El sintetitzador no existeix. ")
    