import json

def main():
    diccionari = {}
    funcio = funcio1(diccionari)
    with open("M10_UF2/Repàs/books.json", "r", encoding="UTF-8") as fitxer:
        llista  = json.load(fitxer)
    print(llista)
    
def funcio1(diccionari):
    diccionari = {"book": [
        {"titel":"Dracula", "cover": "Bram Stoker", "year": 1897, "pages": 576},
        {"titel":"Starship Troopers", "cover": "Robert A. Heinlein", "year": 1959, "pages": 263},
        {"titel":"Harry Potter i la pedra filosofal", "cover": "J. K. Rowling", "year": 1997, "pages": 384},
        {"titel":"Dune", "cover": "Frank Herbert", "year": 1965, "pages": 784}
        ]}
    
    with open("M10_UF2/Repàs/books.json", "w", encoding="UTF-8") as arxiu:
        json.dump(diccionari, arxiu)
    
    return arxiu
if __name__ == "__main__":
    main()