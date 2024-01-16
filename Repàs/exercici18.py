def main():
    

    mT = set()
    input1 = input("Si us plau, introdueixi una paraula: ")
    input2 = input("Si us plau, introdueixi una segona paraula: ")
    
    mT.add(input1)
    mT.add(input2)
    abc = "abcdefghijklmnopqrstuvywxz"
    lista = []
    i = 1
    e = 0

    for a in mT:
        for b in abc:
            if a == b:
                if a in lista:
                    pass
                else:
                    lista[0 + e].append("La lletra", a, " esta repetida: ",  i)
                    i += 1
                    e += 1
            else:
                pass
                
                
            #if mT.count(a) > 1:
        
        
    
    print(lista)
    
    
if __name__ == "__main__":
    main()