def main():
    
    h1 = input("Siusplau introdueixi entre 1 i 3 paraules: ")
    h2 = h1
    
    print(h2)
    i = 0
    #abcde = "abcdefghijklmnopqrstuvwyxz"
    for caracter in enumerate(h2):
        if ' ' in caracter: 
            pass
        else:
            i += 1
                
    
    print("el número total de caràcters és: ", i)
    print("El primer caràcter és: ", h2[0])
    print("L''ultim caràcter és: ", h2[-1])
            
        
        
    
if __name__ == "__main__":
    main()