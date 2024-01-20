def main():
         
    input1 = int(input("Si us plau, introdueix 1 número de l'1 al 10: "))
    i = 1
    a = []
    
    while i < 11:
        b = input1 * i
        a.append(b)
        i += 1
    print(a)
      
if __name__ == "__main__":
    main()