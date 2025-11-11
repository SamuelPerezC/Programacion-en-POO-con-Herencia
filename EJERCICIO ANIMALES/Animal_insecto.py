from Animales import Animales

class animal_insecto(Animales):
    def __init__(self, nombre, edad, habitad, dieta, tamaño, color):
        super().__init__(nombre, edad, habitad, dieta, tamaño, color)

    def moverse(self):
        print("El insecto se moviliza caminando, volando o saltando, según su especie.")

    def comunicacion(self):
        print("El insecto se comunica mediante feromonas, sonidos o movimientos.")

    def reproduccion(self):
        print("El insecto se reproduce de forma sexual, y la mayoría son ovíparos.")

    def adaptacion(self):
        print("El insecto se adapta gracias a su exoesqueleto y su capacidad de metamorfosis.")

    def instintos(self):
        print("El insecto actúa por instinto, guiado por la búsqueda de alimento, refugio y reproducción.")

    def descanso(self):
        print("El insecto descansa en lugares seguros o se mantiene inmóvil durante la noche.")

    def sueño(self):
        print("El insecto entra en un estado de reposo, aunque no sueña como los mamíferos.")

    def interaccion_social(self):
        print("Algunos insectos, como las abejas y hormigas, tienen una estructura social muy organizada.")

    def mostrar_atributos(self):
        print(f"Tipo: Nombre del animal: {self.nombre} - Edad del animal: {self.edad} - Habitad del animal: {self.habitad} - Dieta del animal: {self.dieta} - Tamaño del animal: {self.tamaño} - Color: {self.color}")
