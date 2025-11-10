from Vehiculo import Vehiculo

class Carro_Deportivo(Vehiculo):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)

    def aceleracion(self):
        print("Aceleración deportiva: 0-100 km/h en segundos.")

    def frenado(self):
        print("Frenos de alto rendimiento con ABS deportivo.")

    def sistema_direccion(self):
        print("Dirección deportiva con respuesta inmediata.")

    def climatizacion(self):
        print("Climatización dual zone con asientos ventilados.")

    def tipo_seguridad(self):
        print("Sistema de seguridad deportivo: control de tracción y estabilidad.")

    def luces(self):
        print("Luces LED deportivas con modo carrera.")

    def sistema_ventanas(self):
        print("Ventanas eléctricas con cierre automático.")

    def sistema_espejos(self):
        print("Espejos deportivos plegables eléctricamente.")

    def mostrar_atributos(self):
        print(f"Tipo: Deportivo - Modelo: {self.modelo} - Color: {self.color} - Motor: {self.motor} - Puertas: {self.numero_puertas} - Pasajeros: {self.capacidad_pasajeros} - Combustible: {self.tipo_combustible}")