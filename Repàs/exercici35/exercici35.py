def sumaIlongitut(frase):
    diccionari = {}
    
    for a in frase:
        for b in a:
            if ' ' in b:
                pass
            elif b in diccionari:
                diccionari[b] += 1
            else:
                diccionari[b] = 1

    z = 0
    i = 0
    paraula = ""
    for c in frase:
        for d in c:
            if ' ' in d:
                diccionari[paraula] = i
                z += 1
                i = 0
                paraula = ""
            else:
                paraula += d
                i += 1
                
    if paraula != "":
        diccionari[paraula] = i
        
    return print(diccionari)