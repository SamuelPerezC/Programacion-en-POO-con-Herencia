from Vehiculo import Vehiculo

class Chana_Furgon(Vehiculo):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)

    def aceleracion(self):
        print("Aceleración gradual para carga pesada.")

    def frenado(self):
        print("Sistema de frenos reforzado para carga.")

    def sistema_direccion(self):
        print("Dirección asistida para maniobras con carga.")

    def climatizacion(self):
        print("Climatización básica para espacio amplio.")

    def tipo_seguridad(self):
        print("Sistemas de seguridad básicos para trabajo.")

    def luces(self):
        print("Luces de trabajo adicionales para carga/descarga.")

    def sistema_ventanas(self):
        print("Ventanas manuales, amplias para visibilidad.")

    def sistema_espejos(self):
        print("Espejos grandes para mejor visibilidad de carga.")

    def mostrar_atributos(self):
        print(f"Tipo: Furgón - Modelo: {self.modelo} - Color: {self.color} - Motor: {self.motor} - Puertas: {self.numero_puertas} - Pasajeros: {self.capacidad_pasajeros} - Combustible: {self.tipo_combustible}")