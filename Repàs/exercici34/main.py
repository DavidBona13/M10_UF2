from exercici34 import quadrat2, quadrat

def main():
    a = True
    llista_1 = []
    while a:
        input1 = int(input("Si us plau, introdueix-hi un número: "))
        vari = quadrat(input1)
        print(vari)
        llista_1.append(input1)
        
        b = True
        while b:
            
            input2 = input("Vols afegir més números? [si] o [no] ")
            if input2 == "si":
                b = False
            elif input2 == "no":
                vari2 = quadrat2(quadrat, llista_1)
                b = False
                a = False
            else:
                print("Si us plau, escolleix un opció. ")



if __name__ == "__main__":
    main()