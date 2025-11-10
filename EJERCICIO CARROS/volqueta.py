from Vehiculo import Vehiculo

class Volqueta(Vehiculo):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)

    def arranque(self):
        print("Arranque pesado con precalentamiento para motor diésel.")

    def aceleracion(self):
        print("Aceleración potente pero lenta por el peso.")

    def frenado(self):
        print("Sistema de frenos neumáticos para carga pesada.")

    def sistema_direccion(self):
        print("Dirección hidráulica para vehículos pesados.")

    def climatizacion(self):
        print("Cabina climatizada para largas jornadas.")

    def tipo_seguridad(self):
        print("Sistemas de seguridad avanzados: ABS, control de descenso.")

    def luces(self):
        print("Sistema de iluminación industrial para trabajo nocturno.")

    def sistema_ventanas(self):
        print("Ventanas resistentes con sistema antievaporación.")

    def sistema_espejos(self):
        print("Espejos múltiples para eliminar puntos ciegos.")

    def mostrar_atributos(self):
        print(f"Tipo: Volqueta - Modelo: {self.modelo} - Color: {self.color} - Motor: {self.motor} - Puertas: {self.numero_puertas} - Pasajeros: {self.capacidad_pasajeros} - Combustible: {self.tipo_combustible}")