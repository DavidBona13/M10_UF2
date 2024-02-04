from connection import connexio
from Create_Table import crearTaula
from create import crear
from read import consultar
from update import modificar
from delete import eliminar
import psycopg2

def main():
    try:
        a = True
        b = True
        i = 0
        e = 0
        print("====================================================================================")
        print("Hola, benvingut al menú de consultes de la base de dades PostgreSQL! \n")
        print("Primer s'ha de crear la taula! ")
        connection = connexio()
        con_cursor = connection.cursor()
        
        #bucle pel menu
        while a:
            #Aquest 'if' només servirà per quan s'introdueix incorrectament les dades.
            if i != 0:
                print("Si us plau, introdueix-hi correctament l'opció per poder accedir al menú de consultes. ")
                i = 0
        

            #Creació de la taula (Tot i que en aquest cas, com la taula ja esta creada, faré que si posas 'no' no es tanqui el menú, continui com si l'haguessis creada.)
            while b:
                if e == 0:
                    input1 = input("Vols crear-la? [si] o [no] ")
                    if input1 == "si":
                        variable1 = crearTaula(connection, con_cursor)
                        b = False
                        print("Taula 'SINTETITZADORS' creada correctament! ")
                        e += 1
                    elif input1 == "no":
                        print("====================================================================================\n")
                        print("Si no es crea la taula no és pot seguir! Adèu \n")
                        b = False
                        e += 1
                    else:
                        print("====================================================================================\n")
                        print("Has de seleccionar 'si' o 'no'" )
            
            #Menú de l'aplicació
            print("Benvingut al menú principal! ")
            print("---------------------------------------------- ")
            print("Crear un nou element ========================> [1] ")
            print("Consultar un element existent ===============> [2] ")
            print("Modificar un element existent ===============> [3] ")
            print("Borrar un element existent ==================> [4] ")
            print("Sortir del programa =========================> [5] ")
            input2 = input("Quina consulta desitja fer? ")
            
            if input2 == "1":
                print("====================================================================================")
                print("Has accedit al menú de creació! ")
                creacio = crear(connection, con_cursor)
            elif input2 == "2":
                print("====================================================================================")
                print("Has accedit al menú de consulta! ")
                consulta = consultar(connection, con_cursor) 
            elif input2 == "3":
                print("====================================================================================")
                print("Has accedit al menú de modificació! ")
                update = modificar(connection, con_cursor)
            elif input2 == "4":
                print("====================================================================================")
                print("Has accedit al menú de eliminar un element! ")
                borrar = eliminar(connection, con_cursor)
            elif input2 == "5":
                con_cursor.close()
                print("====================================================================================\n")
                print("Gràcies per consultar la base de dades! ")
                a = False
                break
            else:
                #quan no s'introdueix correctament el número per entrar al menú, vas aqui, el valor 'i' se li suma 1 i vas al if del principi on et diu que introdueixis correctament les dades.
                print("====================================================================================\n")
                print("Has introduït incorrectament les dades. \n")
                i += 1
            
            #Després dels mètodes, fem una consulta al client per si vol continuar o no. Només entrarà en aquest 'if' si s'ha fet una consulta, sino, tornarà al principi del bucle.  
            if input2 == "1" or input2 == "2" or input2 == "3" or input2 == "4":
                while True:
                    input3 = input("Vols fer més consultes? [si] o [no] ")
                    if input3 == "si":
                        break
                        pass
                    elif input3 == "no":
                        con_cursor.close()
                        print("Gràcies per la visita! ")
                        a = False
                        break
                    else:
                        print("Introdueix-hi correctament la resposta ")
    except (Exception, psycopg2.Error) as error:
        print("Error", error)
            
            
    
if __name__ == "__main__":
    main()