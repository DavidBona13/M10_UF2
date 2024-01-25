def operacio(diccionari, input4):
    
    llista_1 = []
    llista_2 = []

    for a, u in diccionari.items():
        
        llista_1.append(a)
        llista_2.append(u)
        
    w = 0
    for z in llista_1:
        #passar l'IVA (per exemple) de 21 a 1.21
        b = input4/100 + 1
        #exemple: preu producte 100 * 1.21
        a = z * b  
        #descompte: 10 a 0.10
        c = llista_2[w] / 100
        #descompte a realitzar 100 * 0.10 = 10
        d = a * c
        #descomptar-li del preu final 100 - 10
        e = a - d
        llista_1[w] = e
        w += 1
    
    p = 1
    for j in llista_1:
        print("Producte ",p,": ", j )
        p += 1
        
    
  
   