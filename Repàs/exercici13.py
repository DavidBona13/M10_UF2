def main():
         
    input1 = int(input("Si us plau, introdueixi 10 números separats per un espais: "))
    i = 1
    a = []
    
    while i < 11:
        b = input1 * i
        a.append(b)
        i += 1
    print(a)
      
if __name__ == "__main__":
    main()