def main():
         
    input1 = int(input("Si us plau, introdueixi un número entre el 10 i el 100: "))
    
    i = 1
    mT = set()
    
    while i <= input1:
        
        if input1 > 9 and input1 < 101:
            mT.add(i)
            i += 1  
        else:
            input1 = int(input("Si us plau, introdueixi un número entre el 10 i el 100: "))
        
    print(mT)
      
    
       
    
if __name__ == "__main__":
    main()