from exercici27 import parametres

def main():
    input1 = int(input("Si us plau, introdueix-hi un número: "))
    input2 = int(input("Si us plau, introdueix-hi el segon número:"))
    
    vari = funcio1(input1, input2)
    print(vari)
    

def funcio1(input1, input2):
    return parametres(input1, input2)
    
    
    
if __name__ == "__main__":
    main()