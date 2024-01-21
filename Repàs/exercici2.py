def main():
    
    a = True
    
    while a:
    
        h1 = int(input("Siusplau introdueixi un valor: "))
        h2 = int(input("Siusplau introdueix l'IVA (4, 10, 21): "))
        
        if h2 == 4:
            print(h1)
            print(h2)
            h3 = h1 * 1.04
            print(h3)
            a = False
        elif h2 == 10:
            print(h1)
            print(h2)
            h3 = h1 * 1.10
            print(h3)
            a = False
        elif h2 == 21:
            print(h1)
            print(h2)
            h3 = h1 * 1.21
            print(h3)
            a = False
        else:
            print("El número utilitzat no forma part del IVA, si us plau, torni a començar correctament. ")
            
if __name__ == "__main__":
    main()