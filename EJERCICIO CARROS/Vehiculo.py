class Vehiculo:
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.numero_puertas = numero_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible

    # métodos
    def arranque(self):
        print("Sistema de arranque activado.")

    def apagado(self):
        print("Sistema de apagado activado.")

    def aceleracion(self):
        print("Sistema de aceleración funcionando.")

    def frenado(self):
        print("Sistema de frenado activado.")

    def sistema_direccion(self):
        print("Sistema de dirección operativo.")

    def climatizacion(self):
        print("Sistema de climatización funcionando.")

    def tipo_seguridad(self):
        print("Sistemas de seguridad activos.")

    def luces(self):
        print("Sistema de iluminación operativo.")

    def sistema_ventanas(self):
        print("Control de ventanas funcionando.")

    def sistema_espejos(self):
        print("Ajuste de espejos disponible.")

    def mostrar_atributos(self):
        print(f"Modelo: {self.modelo} - Color: {self.color} - Motor: {self.motor} - Puertas: {self.numero_puertas} - Pasajeros: {self.capacidad_pasajeros} - Combustible: {self.tipo_combustible}")