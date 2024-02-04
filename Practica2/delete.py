from read import consultar2

def eliminar(connection, con_cursor):
     a = True
     while a:
        input1 = input("Si us plau, introdueix-hi el nom del sintetitzador que vols eliminar ")
        vari1 = consultar2(connection, con_cursor, input1)
        
        if vari1:
            sql = """DELETE FROM public.sintetitzadors WHERE nom = %s"""
            con_cursor.execute(sql, (input1,))
            connection.commit()
            print("Sintetitzador eliminat del sistema! ")
            a = False
        else:
            print("====================================================================================\n")
            print("El sintetitzador no existeix a la base de dades! ")
    