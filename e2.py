class Personajes:
    def __init__(self,nombre,fuerza,inteligencia,defensa,vida):
        self.__nombre=nombre
        self.__fuerza=fuerza
        self.__inteligencia=inteligencia
        self.__defensa=defensa
        self.__vida=vida

    def atributos(self):
        print(self.__nombre,"",sep="")
        print(f"Fuerza {self.__fuerza}")
        print(f"Inteligencia {self.__inteligencia}")
        print(f"Defensa {self.__defensa}")
        print(f"Vida {self.__vida}")

    def subir_nivel(self,fuerza,inteligencia,defensa):
        self.__fuerza=self.__fuerza+fuerza
        self.__inteligencia=self.__inteligencia+inteligencia
        self.__defensa=self.__defensa+defensa

    def esta_vivo(self):
        return self.__vida>0

    def __morir(self):
        self.__vida=0
        print(f"{self.__nombre} ha muerto ")

    def daño(self,enemigo):
        daño = self.__fuerza-enemigo.__defensa
        if daño<0:
            daño=0
        return daño

    def atacar(self,enemigo):
        daño=self.daño(enemigo)
        enemigo.__vida=enemigo.__vida-daño
        print(f"{self.__nombre} ha realizado {daño} puntos de daño a {enemigo.__nombre}")

        if enemigo.esta_vivo():
            print(f"la vida de {enemigo.__nombre} es {enemigo.__vida} ")
        else:
            enemigo.__morir()    

    def get_fuerza(self):
        return self.__fuerza
    def set_fuerza(self,fuerza):
        if fuerza<0:
             print("Error,has introducido un valor negativo")
        else:
            self.__fuerza=fuerza            
 

ultramarin=Personajes("ultramarin",100,50,400,1000)

ogro=Personajes("ogro_comun",50,10,60,500)


fuerza=ultramarin.get_fuerza()

print(f"fuerza {fuerza}")



ultramarin.set_fuerza(1000)

fuerza=ultramarin.get_fuerza()

print(fuerza)



ultramarin.atributos()

for i in range(1,14):
    print(f"turno {i}")
    ultramarin.atacar(ogro)



ultramarin.__fuerza=10000

print(ultramarin.__fuerza)