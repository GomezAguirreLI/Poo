class Celular:
    #metodo constructor
    def __init__(self,marca,modelo,camara):
        #Atributos
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    #Metodos
    def llamar(self):
        print(f"Estas llamando desde tu  {self.modelo}")
    
    def cortar(self):
        print(f"Cortaste la llamada desde tu {self.modelo}")



celuar1=Celular("Samsung","S23","48mp")
celuar2=Celular("Apple","Iphone 15 pro","96mp")        

print(celuar1.marca) 

celuar1.llamar()