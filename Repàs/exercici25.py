from Vehicle import Vehicle
    
def main():
    v = Vehicle([], [], [], [], [], [])
    v = Vehicle("Renault", "Megane", 27.515, "Negre", 200, 5 )
    v.parts()
    print(v.to_dict())
    
if __name__=="__main__":
    main()