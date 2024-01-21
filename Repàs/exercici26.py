from user import User
    
def main():
    v = User([], [], [], [], [], [])
    v = User("Kylian", "Mbappe", "Junio", "kylianjuni@gmail.com", "KyLiAnCiTo33", "********" )
    v.salutacio()
    print(v.to_dict())
    
if __name__=="__main__":
    main()