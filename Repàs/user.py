class User():
    def __init__(self, nom, cognom, cognom2, mail, nom_user, password):
        self._nom = nom
        self._cognom = cognom
        self._cognom2 = cognom2
        self._mail = mail
        self._nom_user = nom_user 
        self._password = password
        
    @property
    def getNom(self):
        return self._nom
    
    @property
    def getCognom(self):
        return self._cognom
        
    @property
    def getCognom2(self):
        return self._cognom2
        
    @property
    def getMail(self):
        return self._mail
        
    @property
    def getNom_user(self):
        return self._nom_user
        
    @property
    def getPassword(self):
        return self._password
        
    
    def setNom(self, nom):
        self._nom = nom
        
    def setCognom(self, cognom):
        self._cognom = cognom
        
    def setCognom2(self, cognom2):
        self._cognom2 = cognom2
        
    def setMail(self, mail):
        self._mail = mail
            
    def setNom_user(self, nom_user):
        self._nom_user = nom_user
        
    def setPassword(self, password):
        self._password = password  
            
    def salutacio(self):
        print("El nom: " +  self._nom)
        print("El primer cognom: " + self._cognom)
        print("El segon cognom: " , self._cognom2)
        print("El correu electrònic: " + self._mail)
        print("El nom d'usuari: " , self._nom_user)
        print("La contrasenya és: " , self._password)
            
        
    def to_dict(self):
        return {"Nom": self._nom, "Cognom": self._cognom, "Segon cognom": self._cognom2, "Mail": self._mail, "Nom usuari": self._nom_user, "Password": self._password}