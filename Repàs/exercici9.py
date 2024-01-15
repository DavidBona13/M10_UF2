def main():
    input1 = input("Siusplau, introdueixi la primera paraula: ")
    input2 = input("Ara la segonda: ")
  
    h1 = input1 
    h2 = input2
   
    h3 = h2[:2] + h1[2:]
    h4 = h1[:2] + h2[2:]
 
    print(h3, " ", h4)
    
if __name__ == "__main__":
    main()