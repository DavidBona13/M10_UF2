import json

def main():
    llista = []
    funcio = funcio1(llista)
    print(funcio)
    
    
def funcio1(llista):
    with open("M10_UF2/Repàs/books.json", "r", encoding="UTF-8") as fitxer:
        llista  = json.load(fitxer)
    return llista


if __name__ == "__main__":
    main()