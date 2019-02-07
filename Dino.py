
class Dino:
    def __init__(self, un_nombre, un_color):
        self.nombre = un_nombre
        self.color = un_color
        print("Hola soy un dinosaurio me llamo", self.nombre, "y soy de color", self.color)

    def rugir(self, rugido):
        print(self)
        print("rawr", Rugido)

    def cambiar_color(self, un_color):
        self.color = un_color

    def que_color(self):
        print("El color del dinosaurio es ", self.color)

#Aca instanciamos o creamos el objeto pepito de tipo Dino
pepito = Dino("Pepe", "Verde")
#Aca accedemos a la propiedad o atributo nombre del objeto e imprimimos
print(pepito.nombre)
#Aca accedemos a la propiedad o atributo nombre del objeto e imprimimos
print(pepito.color)
#Aca llamamos al metodo rugir pasandole una string como atributo
pepito.rugir("AAAAAh")
#
pepito.cambiar_color("lila")

print(pepito.color)


pepito = Dino("Pepe", "Azul")
pepita = Dino("Pepa", "Rojo")
pepite = Dino("pepx")
pepito.nuevo_color("Verde")
pepo = Dino(un_color="Rosa", un_nombre="Pepo")

#







