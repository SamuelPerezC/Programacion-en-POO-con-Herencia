from Animales import Animales

class animal_pez(Animales):
    def __init__(self, nombre, edad, habitad, dieta, tamaño, color):
        """
        Constructor de la clase animal_pez
        Hereda de Animales y especializa comportamientos de peces
        Parámetros:
            nombre: Identificador del pez
            edad: Tiempo de vida
            habitad: Medio acuático (mar, río, lago)
            dieta: Alimentación (carnívoro, herbívoro, omnívoro)
            tamaño: Dimensiones del pez
            color: Coloración para camuflaje o identificación
        """
        super().__init__(nombre, edad, habitad, dieta, tamaño, color)

    def moverse(self):
        """
        Controla la locomoción acuática del pez
        Movimientos ondulantes usando cuerpo y aletas
        """
        print("El pez se moviliza nadando con movimientos ondulantes de su cuerpo y aletas.")

    def comunicacion(self):
        """
        Gestiona la comunicación no vocal de los peces
        Usan señales visuales, químicas y de movimiento
        """
        print("El pez se comunica mediante movimientos, colores y señales químicas.")

    def reproduccion(self):
        """
        Administra la reproducción ovípara de los peces
        La mayoría de peces son ovíparos con fertilización externa
        """
        print("El pez se reproduce generalmente poniendo huevos (ovíparo).")

    def adaptacion(self):
        """
        Maneja las adaptaciones para vida acuática
        Branquias para respirar y cuerpo hidrodinámico
        """
        print("El pez se adapta al agua gracias a sus branquias y a su cuerpo hidrodinámico.")

    def instintos(self):
        """
        Controla los comportamientos instintivos de supervivencia
        Búsqueda de alimento y evasión de depredadores
        """
        print("El pez actúa por instinto, buscando alimento y evitando depredadores.")

    def descanso(self):
        """
        Regula los períodos de reducción de actividad
        Los peces no duermen como los mamíferos pero reducen actividad
        """
        print("El pez reduce su actividad para descansar, flotando o escondiéndose entre rocas o plantas.")

    def sueño(self):
        """
        Gestiona los estados de reposo de los peces
        No tienen párpados pero entran en estados de descanso
        """
        print("El pez entra en un estado de descanso, aunque no cierra los ojos porque no tiene párpados.")

    def interaccion_social(self):
        """
        Administra el comportamiento social en cardúmenes
        Muchos peces forman grupos para protección y alimentación
        """
        print("Algunas especies de peces viven en cardúmenes, lo que les ayuda a protegerse y buscar alimento.")

    def mostrar_atributos(self):
        """
        Muestra todos los atributos del pez en formato específico
        """
        print(f"Tipo: Pez - Nombre: {self.nombre} - Edad: {self.edad} - Hábitat: {self.habitad} - Dieta: {self.dieta} - Tamaño: {self.tamaño} - Color: {self.color}")

    # MÉTODOS ADICIONALES ESPECÍFICOS PARA PECES
    def respirar_agua(self):
        """
        Proceso específico de respiración bajo el agua
        Intercambio de gases a través de las branquias
        """
        print("El pez respira oxígeno disuelto en el agua mediante sus branquias.")

    def cambiar_color(self):
        """
        Capacidad de algunos peces para cambiar coloración
        Usado para camuflaje, comunicación o cambios emocionales
        """
        print("Algunos peces pueden cambiar su coloración para camuflarse o comunicarse.")
