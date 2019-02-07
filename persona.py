#crear una persona que se llame clases y adentro poner los
#archivos dino.py y persona.py
#crear una clase Persona() que tenga como 
#atributos nombre, edad y profesion.
#Al instanciar la clase tiene que saludar igual que el dino diciendo sus atributos

# class persona:
#     def __init__(self, nombre, edad, profesion):
#         self.apodo = nombre
#         print("me llamo", nombre, "tengo", edad, "anhos", "y soy", profesion)


# per1 = persona("Sol", "23", "Programmer")
# print(per1)

# print(per1.apodo) 

# #----------------------------------------------------------------------

# class persona:
#     def __init__(self, un_nombre="", una_edad="", una_profesion="") #nombre="" le da un valor de vacio para que no salga error
#     self.nombre = un_nombre
#     self.edad = una_edad
#     self.profesion = una_profesino
#     prin("hola, mi nombre es", nombre, "tengo", una_edad, "anhos y soy", una_profesion)

# student = persona("Anonimo", 22, "futbolista")

#----------------------------------------------------------------------
#GIT
#github gitlab bitbucket, kinda like a portfolio

#----------------------------------------------------------------------

# Agregar un metodo a la clase persona, que se llame cumpleanhos y que aumente
# la edad de la persona en un anho, y retorne la edad nueva


class persona:
    def __init__(self, un_nombre="", una_edad=0, una_profesion=""): #nombre="" le da un valor de vacio para que no salga error
        self.nombre = un_nombre
        self.edad = una_edad
        self.profesion = una_profesion
        print("hola, mi nombre es", self.nombre, "tengo", str(self.edad), "anhos y soy", self.profesion)

    def cumple(self):
        self.edad = self.edad + 1
        return self.edad

person = persona("Anonimo", 22, "futbolista")

#---------------------------------------------------------------------

class Bootcamp:
    def __init__(self, edad):
        self.edad = edad             #le damos el atributo/caracteristica edad al objeto
        print(edad)                  #self.edad es para utilizar la caracteristica dentro del objeto

    def suma(self):
        self.edad = self.edad + 1
        return self.edad

Penguin = Bootcamp(4)
print(Penguin.suma())

print(Penguin.edad)

#------------------------------------------------------------------------






