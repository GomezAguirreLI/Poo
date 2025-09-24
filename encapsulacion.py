class Personajes:
    def __init__(self,nombre,fuerza,inteligencia,defensa,vida):
        self.nombre=nombre
        self.fuerza=fuerza
        self.inteligencia=inteligencia
        self.defensa=defensa
        self.__vida=vida

    def atributos(self):
        print(self.nombre,"",sep="")
        print(f"Fuerza {self.fuerza}")
        print(f"Inteligencia {self.inteligencia}")
        print(f"Defensa {self.defensa}")
        print(f"Vida {self.vida}")

    def subir_nivel(self,fuerza,inteligencia,defensa):
        self.fuerza=self.fuerza+fuerza
        self.inteligencia=self.inteligencia+inteligencia
        self.defensa=self.defensa+defensa

    def esta_vivo(self):
        return self.vida>0

    def __morir(self):
        self.vida=0
        print(f"{self.nombre} ha muerto ")

    def daño(self,enemigo):
        daño = self.fuerza-enemigo.defensa
        if daño<0:
            daño=0
        return daño

    def atacar(self,enemigo):
        daño=self.daño(enemigo)
        enemigo.vida=enemigo.vida-daño
        print(f"{self.nombre} ha realizado {daño} puntos de daño a {enemigo.nombre}")

        if enemigo.esta_vivo():
            print(f"la vida de {enemigo.nombre} es {enemigo.vida} ")
        else:
            enemigo.__morir()    

            


ultramarin=Personajes("ultramarin",100,50,400,1000)

ogro=Personajes("ogro_comun",50,10,60,500)



'''
for i in range(1,14):
    print(f"turno {i}")
    ultramarin.atacar(ogro)



'''
