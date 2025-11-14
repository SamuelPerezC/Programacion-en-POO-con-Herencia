class Animales:
    def __init__(self, nombre, edad, habitad, dieta, tamaño, color):
        self.nombre = nombre
        self.edad = edad
        self.habitad = habitad
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color

    # métodos
    def moverse(self):
        print("El animal se está moviendo.")

    def comunicacion(self):
        print("El animal se está comunicando.")

    def reproduccion(self):
        print("El animal se está reproduciendo.")

    def adaptacion(self):
        print("El animal se está adaptando.")

    def instintos(self):
        print("Instintos animales activados.")

    def descanso(self):
        print("El animal está descansando.")

    def sueño(self):
        print("El animal está durmiendo.")

    def interaccion_social(self):
        print("El animal está interactuando socialmente.")

    def mostrar_atributos(self):
        print(f"Nombre: {self.nombre} - Edad: {self.edad} - Hábitat: {self.habitad} - Dieta: {self.dieta} - Tamaño: {self.tamaño} - Color: {self.color}")