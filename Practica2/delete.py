from read import consultar2

def eliminar(connection, con_cursor):
     a = True
     #Primer fem la comprovació per si el sintetitzador es o no dins la base de dades. Si no hi és, s'ha de tornar a buscar un altre sintetitzador.
     while a:
         #Comprovem si existeix cridant el mètode 'consultar2' que retorna el sintetitzador
        input1 = input("Si us plau, introdueix-hi el nom del sintetitzador que vols eliminar ")
        vari1 = consultar2(connection, con_cursor, input1)
        
        #Si existeix entra al 'if' i et fa l'operació, sino, et diu que no existeix.
        if vari1:
            sql = """DELETE FROM public.sintetitzadors WHERE nom = %s"""
            con_cursor.execute(sql, (input1,))
            connection.commit()
            print("Sintetitzador eliminat del sistema! ")
            a = False
        else:
            print("====================================================================================\n")
            print("El sintetitzador no existeix a la base de dades! ")
    