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
        print("Movimiento animal ejecutandose")

    def comunicacion():
        print("Metodo de comunicacion animal ejecutandose")

    def reproducción():
        print("Tipo de apareamiento ejecutandose")

    def adaptacion():
        print("Adaptacion al entorno ambiental activado")

    def instintos():
        print("Instinto animal activandose")

    def descanso():
        print("Tiempo de sueño o descanso animal activado")

    def sueño():
        print("Tiempo de sueño activado")

    def interaccion_social():
        print("Interaccion con su entorno activandose")

    def mostrar_atributos(self):
        print(f"Nombre: {self.nombre} - Edad: {self.edad} - Habitad: {self.habitad} - Dieta: {self.dieta} - Tamaño: {self.tamaño} - Color: {self.color}")