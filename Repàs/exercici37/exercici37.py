ftotal = input('Introdueix el preu de tot el carrito:')

vari = amb_iva(ftotal, iva)
print(vari)

def amb_iva(ftotal,iva=21):
    ftotal = ftotal * iva
    return ftotal