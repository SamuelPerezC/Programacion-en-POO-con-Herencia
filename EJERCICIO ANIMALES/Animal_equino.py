from Animales import Animales

class animal_equino(Animales):
    def __init__(self, nombre, edad, habitad, dieta, tamaño, color):
        """
        Constructor de animales equinos (caballos, burros, etc.)
        Hereda todos los atributos de la clase base Animales
        """
        super().__init__(nombre, edad, habitad, dieta, tamaño, color)

    def moverse(self):
        """Movimiento característico de los equinos - galope"""
        print("El equino se moviliza galopando.")

    def comunicacion(self):
        """Comunicación vocal típica de equinos"""
        print("El equino se comunica a través de relinchos.")

    def reproduccion(self):
        """Proceso reproductivo de los equinos"""
        print("El equino se reproduce (macho + hembra).")

    def adaptacion(self):
        """Adaptación basada en el pelaje según el clima"""
        print("El equino se adapta según su pelaje.")

    def instintos(self):
        """Instintos naturales y capacidad de domesticación"""
        print("Por naturaleza el equino es salvaje, pero se puede domar.")

    def descanso(self):
        """Postura característica de descanso equino"""
        print("Los equinos descansan de pie.")

    def sueño(self):
        """Patrones de sueño de los equinos"""
        print("Los equinos tienden a soñar.")

    def interaccion_social(self):
        """Comportamiento social de equinos domesticados"""
        print("Los equinos bien domados, tienden a tener buena interacción social.")

    def mostrar_atributos(self):
        """Muestra atributos específicos de equinos"""
        print(f"Tipo: Equino - Nombre: {self.nombre} - Edad: {self.edad} - Hábitat: {self.habitad} - Dieta: {self.dieta} - Tamaño: {self.tamaño} - Color: {self.color}")
