from Animales import Animales

class animal_pez(Animales):
    def __init__(self, nombre, edad, habitad, dieta, tamaño, color):
        super().__init__(nombre, edad, habitad, dieta, tamaño, color)

    def moverse(self):
        print("El pez se moviliza nadando con movimientos ondulantes de su cuerpo y aletas.")

    def comunicacion(self):
        print("El pez se comunica mediante movimientos, colores y señales químicas.")

    def reproduccion(self):
        print("El pez se reproduce generalmente poniendo huevos (ovíparo).")

    def adaptacion(self):
        print("El pez se adapta al agua gracias a sus branquias y a su cuerpo hidrodinámico.")

    def instintos(self):
        print("El pez actúa por instinto, buscando alimento y evitando depredadores.")

    def descanso(self):
        print("El pez reduce su actividad para descansar, flotando o escondiéndose entre rocas o plantas.")

    def sueño(self):
        print("El pez entra en un estado de descanso, aunque no cierra los ojos porque no tiene párpados.")

    def interaccion_social(self):
        print("Algunas especies de peces viven en cardúmenes, lo que les ayuda a protegerse y buscar alimento.")

    def mostrar_atributos(self):
        print(f"Tipo: Nombre del animal: {self.nombre} - Edad del animal: {self.edad} - Habitad del animal: {self.habitad} - Dieta del animal: {self.dieta} - Tamaño del animal: {self.tamaño} - Color: {self.color}")
