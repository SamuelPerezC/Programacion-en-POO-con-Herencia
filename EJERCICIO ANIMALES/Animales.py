class Animales:
    def __init__(self, nombre, edad, habitad, dieta, tamaño, color):
        """
        Constructor de la clase base Animales
        Inicializa los atributos fundamentales de cualquier animal
        """
        self.nombre = nombre      # Nombre identificador del animal
        self.edad = edad          # Edad en años/meses según corresponda
        self.habitad = habitad    # Entorno natural donde vive
        self.dieta = dieta        # Tipo de alimentación (herbívoro, carnívoro, etc.)
        self.tamaño = tamaño      # Dimensiones físicas del animal
        self.color = color        # Coloración principal

    # MÉTODOS DE COMPORTAMIENTO ANIMAL BÁSICO

    def moverse(self):
        """Controla la locomoción y desplazamiento del animal"""
        print("Movimiento animal ejecutándose")

    def comunicacion(self):
        """Gestiona los métodos de comunicación entre individuos"""
        print("Método de comunicación animal ejecutándose")

    def reproduccion(self):
        """Administra los procesos reproductivos de la especie"""
        print("Tipo de apareamiento ejecutándose")

    def adaptacion(self):
        """Maneja la adaptación al entorno ambiental"""
        print("Adaptación al entorno ambiental activado")

    def instintos(self):
        """Controla los comportamientos instintivos naturales"""
        print("Instinto animal activándose")

    def descanso(self):
        """Regula los períodos de descanso y reposo"""
        print("Tiempo de sueño o descanso animal activado")

    def sueño(self):
        """Gestiona los ciclos de sueño del animal"""
        print("Tiempo de sueño activado")

    def interaccion_social(self):
        """Administra las interacciones con otros animales"""
        print("Interacción con su entorno activándose")

    def mostrar_atributos(self):
        """Muestra todos los atributos del animal en formato legible"""
        print(f"Nombre: {self.nombre} - Edad: {self.edad} - Hábitat: {self.habitad} - Dieta: {self.dieta} - Tamaño: {self.tamaño} - Color: {self.color}")
