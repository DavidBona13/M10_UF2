def main():
    areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]
    
    print("Segon element: ", areas_pis[1])
    print("Últim element: ",areas_pis[13])
    print("Àrea de Terrasa", areas_pis[7])
    print("Del primer element a l'últim: ",areas_pis[0], areas_pis[1], areas_pis[2])
    lista = []
    for i in areas_pis:
        if i == "Menjador" or i == 10.15:
            pass
        else:
            lista.append(i)
    print("Del tercer a l'últim element: ", lista)
        
    v = areas_pis[5] + areas_pis[13]
    print("Àrea total de les dues habitacions: ", v)
    
    areas_pis[10] = 13.65
    print("La nova àrea del lavabo: ", areas_pis[10])
    
    areas_pis.append("pati interior")
    areas_pis.append(2.78)
    print("El pati interior i la seva àrea: ", areas_pis)
    
    total = areas_pis[1] + areas_pis[3] + areas_pis[5] + areas_pis[7] + areas_pis[9] + areas_pis[11] + areas_pis[13] + areas_pis[15]
    print("Àrea total del pis: ", total)
    
if __name__ == "__main__":
    main()