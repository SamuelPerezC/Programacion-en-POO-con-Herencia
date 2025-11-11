from Animales import Animales

class animal_equino(Animales):
    def __init__(self, nombre, edad, habitad, dieta, tamaño, color):
        super().__init__(nombre, edad, habitad, dieta, tamaño, color)

    def moverse(self):
        print("El equino se moviliza galopando.")

    def comunicacion(self):
        print("El equino se comunica a travez de relinchos.")

    def reproduccion(self):
        print("El equino se reproduce (macho + hembra).")

    def adaptacion(self):
        print("El equino se adapta segun su pelaje.")

    def instintos(self):
        print("Por naturaleza el equino es salvaje, pero se puede domar.")

    def descanso(self):
        print("Los equinos descansan de pie.")

    def sueño(self):
        print("Los equinos tienden a soñar.")

    def interaccion_social(self):
        print("Los equinos bien domados, tienden a tener buena interaccion social.")

    def mostrar_atributos(self):
        print(f"Tipo: Nombre del animal: {self.nombre} - Edad del animal: {self.edad} - Habitad del animal: {self.habitad} - Dieta del animal: {self.dieta} - Tamaño del animal: {self.tamaño} - Color: {self.color}")