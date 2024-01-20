def main():
    

    mT = []
    input1 = input("Si us plau, introdueixi una paraula: ")
    input2 = input("Si us plau, introdueixi una segona paraula: ")
    
    mT.append(input1)
    mT.append(input2)
    lista = {}

    for a in mT:
        for b in a:
            if b in lista:
                lista[b] += 1
            else:
                lista[b] = 1
        
    lista = tuple(lista.items())
    print(lista)
    
    
if __name__ == "__main__":
    main()