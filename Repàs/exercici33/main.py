from exercici33 import operacio
def main():
    a = True
    diccionari ={}
    while a:
        input1 = float(input("Si us plau, introdueix-hi el preu d'un producte sense l'IVA: "))
        input2 = int(input("Si us plau, introdueix-hi el descompte desitjat: "))
        
        diccionari[input1] = input2
        b = True

        while b:
            input3 = input("Vols continua introduint productes? ([si] o [no])")
            
            if input3 == "no":
                input4 = int(input("Si us plau, intrudeix-hi l'IVA desitjat: "))
                vari = operacio(diccionari, input4)
                a = False
                b = False
            elif input3 == "si":
                b = False
            else:
                print("Introdueix-hi correctament les dades [si] o [no] ")
    
if __name__ == "__main__":
    main()