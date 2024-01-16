def main():
         
    input1 = int(input("Si us plau, introdueixi un número entre el 0 i el 12: "))
   
    mT = ('Gener', 'Febrer', 'Març', 'Abril', 'Maig', 'Juny', 'Juliol', 'Agost', 'Septembre', 'Octubre', 'Novembre', 'Decembre')
    a = True
    
    while a:
        
        if input1 > 0 and input1 <= 12:
            print(mT[input1 - 1])
            input1 = int(input("Si us plau, introdueixi un número entre el 0 i el 12: "))
        elif input1 == 0:
            print("Final de programa")
            a = False
      
if __name__ == "__main__":
    main()