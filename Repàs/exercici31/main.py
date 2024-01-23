from exercici31 import calcularIva
def main():
    input1 = float(input("Si us plau, introdueix-hi el preu del producte o servei sense l'IVA: "))
    input2 = int(input("Si us plau, introdueix-hi l'IVA: (4, 10 o 21) "))
    
    if input2 != 4 and input2 != 10 and input2 != 21:
        input2 = 21
        vari = funcio1(input1, input2)
    else:
        vari = funcio1(input1, input2)
    
    print("El valor sense IVA és el següent: ", input1)
    print("L'IVA introduït és: ", input2)
    print("El valor total del producte o servei és de ", vari, " euros.")
    
    
def funcio1(input1, input2):
    return calcularIva(input1, input2)


if __name__ == "__main__":
    main()