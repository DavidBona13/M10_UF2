def main():
    
    lista = []
    mT = set()
    i = 0
    
    while  i <= 10:
        input1 = int(input("Si us plau, introdueixi un número entre el 1 i el 10: "))
        lista.append(input1)
        i += 1
  
    #lista.sort()
    sorted(lista)

    for a in lista:
        mT.add(a)
    
    print(mT)
    
if __name__ == "__main__":
    main()