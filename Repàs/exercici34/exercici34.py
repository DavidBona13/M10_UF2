
def quadrat(input1):
    a = input1 * input1
    return a

def quadrat2(quadrat, llista):
    nova_llista = []
    for i in llista:
        vari = quadrat(i)
        nova_llista.append(vari)
    print(nova_llista)