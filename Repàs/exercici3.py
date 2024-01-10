def main():
    
    h1 = int(input("Siusplau introdueixi el valor 1: "))
    h2 = int(input("Siusplau introdueix el valor 2: "))
    
    if h1 < h2:
        print(h2 , " és més gran que " , h1)
    elif h1 > h2:
        print(h1 , " és més gran que " , h2)
    else:
        print(h1 , " i ", h2, " son iguals. ")
            
if __name__ == "__main__":
    main()