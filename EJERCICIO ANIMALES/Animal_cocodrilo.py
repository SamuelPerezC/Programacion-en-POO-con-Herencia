from Animales import Animales

class animal_cocodrilo(Animales):
    def __init__(self, nombre, edad, habitad, dieta, tamaño, color):
        super().__init__(nombre, edad, habitad, dieta, tamaño, color)

    def moverse(self):
        print("El cocodrilo se moviliza reptando o nadando silenciosamente.")

    def comunicacion(self):
        print("El cocodrilo se comunica mediante rugidos, gruñidos y sonidos guturales.")

    def reproduccion(self):
        print("El cocodrilo se reproduce de manera sexual, poniendo huevos.")

    def adaptacion(self):
        print("El cocodrilo se adapta a su entorno acuático y terrestre gracias a su piel gruesa y resistente.")

    def instintos(self):
        print("El cocodrilo es un cazador nato con fuertes instintos depredadores.")

    def descanso(self):
        print("El cocodrilo descansa al sol para regular su temperatura corporal.")

    def sueño(self):
        print("El cocodrilo duerme con un ojo abierto, manteniéndose alerta ante el peligro.")

    def interaccion_social(self):
        print("Los cocodrilos son territoriales, pero pueden convivir pacíficamente en áreas de abundante alimento.")

    def mostrar_atributos(self):
        print(f"Tipo: Nombre del animal: {self.nombre} - Edad del animal: {self.edad} - Habitad del animal: {self.habitad} - Dieta del animal: {self.dieta} - Tamaño del animal: {self.tamaño} - Color: {self.color}")
