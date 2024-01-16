def main():
    

    mT = set()
    input1 = input("Si us plau, introdueixi una frase: ")
    
    vari = funcio1(input1, mT)
    print(vari)
    
    
    
def funcio1(input1, mT):
    
    b = ""
    
    for d in input1:
        
        if ' ' in d:
            pass
        else:
            b += d      
            
    mT.add(b)
    
    return mT
    
if __name__ == "__main__":
    main()