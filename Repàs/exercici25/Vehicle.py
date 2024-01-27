class Vehicle():
    def __init__(self, marca, model, preu, color, cavalls, portes):
        self._marca = marca
        self._model = model
        self._preu = preu
        self._color = color
        self._cavalls = cavalls 
        self._portes = portes 
        
    @property
    def getMarca(self):
        return self._marca
    
    @property
    def getModel(self):
        return self._model
        
    @property
    def getPreu(self):
        return self._preu
        
    @property
    def getColor(self):
        return self._color
        
    @property
    def getCavalls(self):
        return self._cavalls
        
    @property
    def getPortes(self):
        return self._portes
        
    
    def setMarca(self, marca):
        self._marca = marca
        
    def setModel(self, model):
        self._model = model
        
    def setPreu(self, preu):
        self._preu = preu
        
    def setColor(self, color):
        self._color = color
            
    def setCavalls(self, cavalls):
        self._cavalls = cavalls 
        
    def setPortes(self, portes):
        self._portes = portes  
            
    def parts(self):
        print("La marca del vehicle és: " +  self._marca)
        print("El model del cotxe és: " + self._model)
        print("El preu de sortida és: " , self._preu)
        print("El color del vehicle és: " + self._color)
        print("Els cavalls del vehile son: " , self._cavalls)
        print("La quantitat de portes del vehicle és de: " , self._portes)
            
        
    def to_dict(self):
        return {"marca": self._marca, "model": self._model, "preu": self._preu, "color": self._color, "cavalls": self._cavalls, "portes": self._portes}