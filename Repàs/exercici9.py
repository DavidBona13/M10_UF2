def main():
    input1 = input("Siusplau, introdueixi la primera paraula: ")
    input2 = input("Ara la segonda: ")
    
    h1 = input1 
    h2 = input2
    h1.replace(h1[0], h2[0])
    h1.replace(h1[1], h2[1])
    #h2.replace(h2[0], h1[0])
    #h2.replace(h2[1], h1[1])
    
    print(h1.replace(h1[0], h2[0]), h2.replace(h2[0], h1[0]))
    
if __name__ == "__main__":
    main()