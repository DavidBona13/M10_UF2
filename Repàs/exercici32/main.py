from exercici32 import quadrats

def main():
    llista = []
    a = True
    i = 1
    while a:
        i = str(i)
        input1 = int(input("Si us plau, introdueix-hi el número "+ i + " de la llista formada per 10 números: "))
        i = int(i)
        i += 1
        llista.append(input1)
        if i == 11:
            vari = funcio1(llista)
            print(vari)
            a = False
    
    
def funcio1(llista):
    return quadrats(llista)


if __name__ == "__main__":
    main()