from exercici38 import elimina
def main():
    contactes = {'Roger': 678232311, 'Oriol': 566879326}
    user = input("Si us plau, introdueix-hi el el nom del usuari que desitjar eliminar: ")
    vari = elimina(contactes, user)
    print(vari)
    print(contactes)
    
if __name__ == "__main__":
    main()