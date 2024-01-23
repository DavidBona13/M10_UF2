from exercici29 import *
def main():
    a = True
    while a:
        input1 = int(input("Si us plau, introdueix-hi un número: "))
        input2 = int(input("Si us plau, introdueix-hi el segon número:"))
        if input1 == input2:
            print("Has introduit dos números iguals, si us plau, introdueix-hi dos números diferents. ")
        else:
            vari = funcio1(input1, input2)
            print(vari)
            vari2 = funcio2(vari)
            print(vari2)
            a = False
    
def funcio1(input1, input2):
    return enters(input1, input2)
    
def funcio2(sumaTotal):
    return suma(sumaTotal)
    
if __name__ == "__main__":
    main()