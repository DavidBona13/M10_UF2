from read import consultar, consultar2
def crear(connection, con_cursor):
    a = True
    while a:
        #El primer que farem és comprovar si l'article ja és dins de la base de dades, per això cridarem un mètode de la classe read.py que ens farà la comprovació
        input1 = input("Si us plau, introdueix-hi el nom del nou sintetitzador que vols afegir ")
        vari1 = consultar2(connection, con_cursor, input1)
        
        #Si hi és dins, has de tornar a posar un altre sintetitzador, fins que trobis un que no estigui dins la base de dades
        if vari1:
            print("====================================================================================\n")
            print("El sintetitzador ja existeix a la base de dades, no es pot tornar a afegir! ")
        else:
            #Inputs de tots els altres elements de la taula, menys l'id, que és SERIAL i és suma automàticament.
            input2 = input("Introdueix-hi la marca: ")
            input3 = input("El tipus de sintesi: ")
            input4 = input("Breu descripció del producte: ")
            input5 = input("Tipus de conexions: ")
            
            sql = """ INSERT INTO public.sintetitzadors(nom, marca, tipus, descripcio, connexions) VALUES(%s, %s, %s, %s, %s)
            """
            #Pasem els inputs dins d'una tupla, si no es fa així dona error.
            con_cursor.execute(sql, (input1, input2, input3, input4, input5))
            connection.commit()
            
            print("Sintetitzador afegit correctament!\n ")
            vari2 = consultar2(connection, con_cursor, input1)
            print(vari2)
            a = False
            