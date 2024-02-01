from connection import connexio
from Create_Table import crear
def main():
    a = True
    b = True
    i = 0
    e = 0
    print("====================================================================================\n")
    print("Hola, benvingut al menú de consultes de la taula *** amb la base de dades PostgreSQL! ")
    connection = connexio()
    
    while a:
        if i != 0:
            print("Si us plau, introdueix-hi correctament l'opció per poder accepdir al menú de consultes. ")
            input1 = input("A quin menú vol accedir? ")
        
        while b:
            if e == 0:
                print("Primer s'ha de crear la taula!\n ")
                input2 = input("Vols crear-la? [si] o [no] ")
                    
                if input2 == "si":
                    variable1 = crear(connection)
                    b = False
                    print("Taula 'SINTETITZADORS' creada correctament! ")
                    e += 1
                elif input2 == "no":
                    print("Si no es crea la taula no és pot seguir! Adèu")
                    a = False
                    b = False
                else:
                    print("====================================================================================\n")
                    print("Has de seleccionar 'si' o 'no'" )

            
            
            
    
if __name__ == "__main__":
    main()