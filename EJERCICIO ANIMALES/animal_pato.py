from Animales import Animales

class Animal_pato(Animales):
    def __init__(self, nombre, edad, habitad, dieta, tamaño, color):
        super().__init__(nombre, edad, habitad, dieta, tamaño, color)

    def moverse(self):
        print("El pato se moviliza caminando, nadando y volando.")

    def comunicacion(self):
        print("El pato se comunica mediante graznidos y otros sonidos característicos.")

    def reproduccion(self):
        print("El pato se reproduce poniendo huevos, usualmente en nidos cerca del agua.")

    def adaptacion(self):
        print("El pato se adapta al agua con su pico ancho y patas palmeadas para nadar fácilmente.")

    def instintos(self):
        print("El pato tiene instintos protectores, especialmente hacia sus crías.")

    def descanso(self):
        print("El pato descansa flotando en el agua o en la orilla, con la cabeza escondida bajo el ala.")

    def sueño(self):
        print("El pato duerme parcialmente alerta, capaz de mantener un ojo abierto ante el peligro.")

    def interaccion_social(self):
        print("Los patos suelen vivir en grupos y son animales sociables y cooperativos.")

    def mostrar_atributos(self):
        print(f"Tipo: Nombre del animal: {self.nombre} - Edad del animal: {self.edad} - Habitad del animal: {self.habitad} - Dieta del animal: {self.dieta} - Tamaño del animal: {self.tamaño} - Color: {self.color}")
