
def enters(input1, input2):
    if input1 < input2:
        i = input1
        llista = []
        while i < input2:
            i += 1
            if i == input2:
                break
            llista.append(i)
        return llista
    else: 
        i = input2
        llista = []
        while i < input1:
            i += 1
            if i == input1:
                break
            llista.append(i)
        return llista
    
def suma(sumaTotal):
    a = 0
    for i in sumaTotal:
        a += i
    return a
        