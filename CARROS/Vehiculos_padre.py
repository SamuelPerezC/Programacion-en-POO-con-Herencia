# Vehiculos_padre.py
class Vehiculos:
    def __init__(self, modelo, color, motor,numero_puertas, capacidad_pasajeros, tipo_combustible ):
        # Atributos
        self.modelo = modelo
        self.color = color  
        self.motor = motor
        self.numero_puertas = numero_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible
        self.encendido = False

        # Métodos         
    def arranque(self):
        if self.encendido:
            print("El vehiculo esta encendido")
        else:
            self.encendido = True
            print("El vehiculo ha arrancado")
        
    def apagado(self):
        if self.encendido:
            self.encendido = False
        else:
            print("motor apagado ")
                
