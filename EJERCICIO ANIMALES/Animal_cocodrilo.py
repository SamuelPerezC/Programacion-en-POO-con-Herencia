from Animales import Animales

class animal_cocodrilo(Animales):
    def __init__(self, nombre, edad, habitad, dieta, tamaño, color):
        """
        Constructor de cocodrilos - reptiles semiacuáticos
        Hereda atributos base y especializa comportamientos
        """
        super().__init__(nombre, edad, habitad, dieta, tamaño, color)

    def moverse(self):
        """Movimiento reptante y natación característicos"""
        print("El cocodrilo se moviliza reptando o nadando silenciosamente.")

    def comunicacion(self):
        """Sistema de comunicación vocal de cocodrilos"""
        print("El cocodrilo se comunica mediante rugidos, gruñidos y sonidos guturales.")

    def reproduccion(self):
        """Reproducción ovípara típica de reptiles"""
        print("El cocodrilo se reproduce de manera sexual, poniendo huevos.")

    def adaptacion(self):
        """Adaptaciones físicas para vida anfibia"""
        print("El cocodrilo se adapta a su entorno acuático y terrestre gracias a su piel gruesa y resistente.")

    def instintos(self):
        """Instintos depredadores altamente desarrollados"""
        print("El cocodrilo es un cazador nato con fuertes instintos depredadores.")

    def descanso(self):
        """Comportamiento de termorregulación durante el descanso"""
        print("El cocodrilo descansa al sol para regular su temperatura corporal.")

    def sueño(self):
        """Patrón de sueño alerta característico de depredadores"""
        print("El cocodrilo duerme con un ojo abierto, manteniéndose alerta ante el peligro.")

    def interaccion_social(self):
        """Comportamiento territorial y social en grupos"""
        print("Los cocodrilos son territoriales, pero pueden convivir pacíficamente en áreas de abundante alimento.")

    def mostrar_atributos(self):
        """Muestra atributos específicos de cocodrilos"""
        print(f"Tipo: Cocodrilo - Nombre: {self.nombre} - Edad: {self.edad} - Hábitat: {self.habitad} - Dieta: {self.dieta} - Tamaño: {self.tamaño} - Color: {self.color}")
