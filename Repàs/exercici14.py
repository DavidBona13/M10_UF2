def main():
    
    lista = []
    mT = []
    i = 0
    
    while  i <= 10:
        input1 = int(input("Si us plau, introdueixi un número entre el 1 i el 10: "))
        lista.append(input1)
        i += 1
  
    lista.sort()

    for a in lista:
        mT.append(a)
        
    mT = tuple(mT)
    print(mT)
    
if __name__ == "__main__":
    main()