from Animales import Animales

class Animal_pato(Animales):
    def __init__(self, nombre, edad, habitad, dieta, tamaño, color):
        """
        Constructor de la clase Animal_pato
        Hereda de la clase base Animales y especializa comportamientos de aves acuáticas
        Parámetros:
            nombre: Identificador del pato
            edad: Tiempo de vida del pato
            habitad: Entorno donde vive (lagos, ríos, estanques)
            dieta: Tipo de alimentación (omnivoro)
            tamaño: Dimensiones físicas
            color: Plumaje característico
        """
        super().__init__(nombre, edad, habitad, dieta, tamaño, color)

    def moverse(self):
        """
        Controla la locomoción tridimensional del pato
        Los patos pueden caminar, nadar y volar
        """
        print("El pato se moviliza caminando, nadando y volando.")

    def comunicacion(self):
        """
        Gestiona los métodos de comunicación vocal del pato
        Los patos usan graznidos para comunicarse
        """
        print("El pato se comunica mediante graznidos y otros sonidos característicos.")

    def reproduccion(self):
        """
        Administra el proceso reproductivo del pato
        Los patos son ovíparos y construyen nidos cerca del agua
        """
        print("El pato se reproduce poniendo huevos, usualmente en nidos cerca del agua.")

    def adaptacion(self):
        """
        Maneja las adaptaciones físicas para vida acuática
        Pico ancho para filtrar alimento y patas palmeadas para nadar
        """
        print("El pato se adapta al agua con su pico ancho y patas palmeadas para nadar fácilmente.")

    def instintos(self):
        """
        Controla los comportamientos instintivos de protección
        Fuertes instintos maternales/paternales
        """
        print("El pato tiene instintos protectores, especialmente hacia sus crías.")

    def descanso(self):
        """
        Regula los patrones de descanso del pato
        Descansan flotando en el agua o en tierra firme
        """
        print("El pato descansa flotando en el agua o en la orilla, con la cabeza escondida bajo el ala.")

    def sueño(self):
        """
        Gestiona los ciclos de sueño con mecanismos de alerta
        Sueño unihemisférico para mantenerse alerta
        """
        print("El pato duerme parcialmente alerta, capaz de mantener un ojo abierto ante el peligro.")

    def interaccion_social(self):
        """
        Administra las interacciones sociales grupales
        Los patos son animales gregarios que vien en bandadas
        """
        print("Los patos suelen vivir en grupos y son animales sociables y cooperativos.")

    def mostrar_atributos(self):
        """
        Muestra todos los atributos del pato en formato específico
        Incluye el tipo de animal y todos sus características
        """
        print(f"Tipo: Pato - Nombre: {self.nombre} - Edad: {self.edad} - Hábitat: {self.habitad} - Dieta: {self.dieta} - Tamaño: {self.tamaño} - Color: {self.color}")

    # MÉTODOS ADICIONALES ESPECÍFICOS PARA PATOS
    def bucear(self):
        """
        Comportamiento específico de patos buceadores
        Algunas especies de patos pueden sumergirse completamente
        """
        print("El pato se sumerge en el agua para buscar alimento.")

    def migrar(self):
        """
        Comportamiento migratorio estacional
        Muchas especies de patos migran según las estaciones
        """
        print("El pato realiza migraciones estacionales en busca de climas más favorables.")

    def acicalarse(self):
        """
        Comportamiento de cuidado del plumaje
        Los patos dedican tiempo al acicalamiento para mantener su plumaje impermeable
        """
        print("El pato se acicala las plumas para mantener su impermeabilidad.")
