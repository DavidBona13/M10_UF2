from exercici37 import amb_iva
def main():
    ftotal = float(input('Introdueix el preu de tot el carrito:'))
    iva = 21

    vari = amb_iva(ftotal, iva)
    print(vari)
    
    
if __name__ == "__main__":
    main()