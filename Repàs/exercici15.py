def main():
    
    lista = []
    mT = []
    a = True
    
    while  a:
        
        input1 = int(input("Si us plau, introdueixi un número entre el 1 i el 10: "))
        
        if input1 != 0:
            lista.append(input1)
        else:
            a = False
            
    lista.sort()

    for a in lista:
        mT.append(a)
    
    mT = tuple(mT)
    print("Programa finalitzat")
    print("Aquesta és la quantitat inserida:")
    print(mT)
    
if __name__ == "__main__":
    main()