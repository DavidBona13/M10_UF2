def main():
    
    vari = funcio1()
    with open("M10_UF2/Repàs/arxiu.xml", "r", encoding="UTF-8") as fitxer:
        varianle1 = fitxer.read()
        print(varianle1)
    
    
def funcio1():
    codi ="""<?xml version="1.0" encoding="UTF-8"?>
    <Students>
        <student id="1">
            <name>Xavi</name>
            <surname>Pérez</surname>
            <email>xaviperez@gmail.com</email>
            <dni>58463726D</dni>
        </student>
        <student id="2">
            <name>Josep</name>
            <surname>Doménech</surname>
            <email>josepdo@gmail.com</email>
            <dni>14253748U</dni>
        </student>
        <student id="3"> 
            <name>Lluís</name>
            <surname>Mont</surname>
            <email>lluismont@gmail.com</email>
            <dni>58473625P</dni>
        </student>
        <student id="4">
            <name>Alejandro</name>
            <surname>Vallés</surname>
            <email>alevalle@gmail.com</email>
            <dni>30495867W</dni>
        </student>
        <student id="5">
            <name>Isolda</name>
            <surname>Esposito</surname>
            <email>isiespo@gmail.com</email>
            <dni>09786534G</dni>
        </student>
    </Students>
    """
    with open("M10_UF2/Repàs/arxiu.xml", "w", encoding="UTF-8") as arxiu:
        arxiu.write(codi)
        
    return arxiu
    
if __name__ == "__main__":
    main()