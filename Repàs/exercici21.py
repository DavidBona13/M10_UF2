def main():

    mT = []
    
    vari = funcio1(mT)
    print("Números de l'usuari: ", vari)
    vari2 = funcio2(vari)  
    print("suma total: ", vari2)
    vari3 = funcio3(vari2)
    print("mitjana: ", vari3)
    vari4 = funcio4(vari, vari2, vari3)
    print("Llista amb els números, la suma i la mitjana: ", vari4)
    
    
def funcio1(mT):
    a = True
    i = 0
    while a:
        input1 = int(input("Si us plau, introdueixi un número: "))
        mT.append(input1)
        
        for a in mT:
            i += 1
            if i == 10:
                a = False
        i = 0
    return mT
    
    
def funcio2(mT):
    b = 0
    for a in mT:
        b += a
    return b


def funcio3(a):
    b = a/10
    return b
    
    
def funcio4(vari, vari2, vari3):
    vari.append(vari2)
    vari.append(vari3)
    return vari
    
    
if __name__ == "__main__":
    main()