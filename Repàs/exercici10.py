import random

def main():
    
    numero = random.randint(1, 100)
    i = 0
    b = True
    
    while b == True:
        
        input1 = int(input("Si us plau, torni a introduir un número: "))
        
        if input1 > numero:
            print("El número és més petit. ")
        elif input1 < numero:
            print("El número és més gran. ")
        else:
            print("Enhorabona! l'has encertat.")
            i += 1
            print("Ho has fet amb ", i, " intens! ")
            b = False
            
        i += 1
    
if __name__ == "__main__":
    main()