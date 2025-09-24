#Ejercicio 1
#Crear una clase llamada estudiantes con la instancia estudiante que tenga los atributos nombre,edad y grado con el metodo estudiar se debe interactuar con el usuario y este debe brindar los atributos 




class estudiantes:
    #Metodo constructos
    def __init__(self,nombre,edad,grado):
        self.nombre= nombre
        self.edad=edad
        self.grado=grado

    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando")    


estudiante={
        "nombre":"",
        "edad":"",
        "grado":""
}

estudiante["nombre"]=input("Ingrese el nombre del alumno: ").lower().strip()
estudiante["edad"]=input("Ingrese la edad del alumno: ").lower().strip()
estudiante["grado"]=input("Ingrese el grado del alumno: ").lower().strip()

estudiante1=estudiantes(estudiante["nombre"],estudiante["edad"],estudiante["grado"])

estudiante1.estudiar() 