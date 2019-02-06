#crear una persona que se llame clases y adentro poner los
#archivos dino.py y persona.py
#crear una clase Persona() que tenga como 
#atributos nombre, edad y profesion.
#Al instanciar la clase tiene que saludar igual que el dino diciendo sus atributos

class persona:
    def __init__(self, nombre, edad, profesion):
        self.apodo = nombre
        print("me llamo", nombre, "tengo", edad, "anhos", "y soy", profesion)


per1 = persona("Sol", "23", "Programmer")
print(per1)

print(per1.apodo) 

#----------------------------------------------------------------------

class persona:
    def __init__(self, un_nombre="", una_edad="", una_profesion="") #nombre="" le da un valor de vacio para que no salga error
    self.nombre = un_nombre
    self.edad = una_edad
    self.profesion = una_profesino
    prin("hola, mi nombre es", nombre, "tengo", una_edad, "anhos y soy", una_profesion)

student = persona("Anonimo", 22, "futbolista")

#----------------------------------------------------------------------
#GIT
#github gitlab bitbucket, kinda like a portfolio


