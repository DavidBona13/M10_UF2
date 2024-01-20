def main():
    
    diccio = {}
    a = True
    
    while a:
        
        input1 = input("Si us plau, introdueix un nom: ")
        input2 = int(input("Si us plau, introdueix la seva edat: "))
        
        if input1 in diccio:
            print("Ho sento, aquest nom ja ha sigut introduit anteriorment")
        else: 
            diccio[input1] = input2
            
            input3 = input("Vols continua afegint noms i edats? si o no ")
        
            if input3 == "no":
                a = False
    
    print(diccio)
    
if __name__ == "__main__":
    main()