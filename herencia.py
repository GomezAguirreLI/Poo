class Personas:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad

    def hablar(self):
        print("Hola estoy hablando un poco")

class Artistas:
     def __init__(self,habilidad):
          self.habilidad=habilidad

     def mostrar_habilidades(self):
        print(f"Mi habilidad es:{self.habilidad}")



class EmpleadoArtista(Personas,Artistas):
    def __init__(self, nombre, edad, nacionalidad,habilidad,salario,empresa):
          Personas.__init__(nombre, edad, nacionalidad)
          Artistas.__init__(self,habilidad)
          self.salario=salario
          self.empresa=empresa

    def presentarse(self):

        #Muestra que es un metodo de una clase heredada
        return(f"{super().mostrar_habilidades()}")



class Empleados(Personas):
        def __init__(self, nombre, edad, nacionalidad,trabajo,salario):
             super().__init__(nombre, edad, nacionalidad)
             self.trabajo=trabajo
             self.salario=salario


class Estudiantes(Personas):
        def __init__(self, nombre, edad, nacionalidad,matricula,escuela):
             super().__init__(nombre, edad, nacionalidad)
             self.matricula=matricula
             self.escuela=escuela



roberto=Empleados("li",19,"Mexicano")

gabriel=EmpleadoArtista("gabriel",19,"Mexicano","Fisicocultursita",16000,"Robotics")

gabriel.presentarse

print(roberto.nacionalidad)