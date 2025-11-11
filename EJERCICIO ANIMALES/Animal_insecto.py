from Animales import Animales

class animal_insecto(Animales):
    def __init__(self, nombre, edad, habitad, dieta, tamaño, color):
        """
        Constructor para insectos - artrópodos diversos
        Especializa comportamientos de invertebrados
        """
        super().__init__(nombre, edad, habitad, dieta, tamaño, color)

    def moverse(self):
        """Diversidad de movimientos según tipo de insecto"""
        print("El insecto se moviliza caminando, volando o saltando, según su especie.")

    def comunicacion(self):
        """Sistemas de comunicación química y física"""
        print("El insecto se comunica mediante feromonas, sonidos o movimientos.")

    def reproduccion(self):
        """Reproducción predominante en insectos"""
        print("El insecto se reproduce de forma sexual, y la mayoría son ovíparos.")

    def adaptacion(self):
        """Adaptaciones estructurales y evolutivas"""
        print("El insecto se adapta gracias a su exoesqueleto y su capacidad de metamorfosis.")

    def instintos(self):
        """Comportamientos instintivos básicos de supervivencia"""
        print("El insecto actúa por instinto, guiado por la búsqueda de alimento, refugio y reproducción.")

    def descanso(self):
        """Patrones de reposo en insectos"""
        print("El insecto descansa en lugares seguros o se mantiene inmóvil durante la noche.")

    def sueño(self):
        """Estados de reposo en invertebrados"""
        print("El insecto entra en un estado de reposo, aunque no sueña como los mamíferos.")

    def interaccion_social(self):
        """Comportamiento social en insectos eusociales"""
        print("Algunos insectos, como las abejas y hormigas, tienen una estructura social muy organizada.")

    def mostrar_atributos(self):
        """Muestra atributos específicos de insectos"""
        print(f"Tipo: Insecto - Nombre: {self.nombre} - Edad: {self.edad} - Hábitat: {self.habitad} - Dieta: {self.dieta} - Tamaño: {self.tamaño} - Color: {self.color}")
