# volqueta_hijo.py
from Vehiculos_padre import Vehiculos

class volqueta_hijo(Vehiculos):
    def __init__(self, modelo, color, motor,numero_puertas, capacidad_pasajeros, tipo_combustible, dato_tipo_trabajo):
        super().__init__(modelo, color, motor,numero_puertas, capacidad_pasajeros, tipo_combustible)
        #Atributos para vehiculo de carga
        self.tipo_trabajo_pesado = dato_tipo_trabajo
        
    def activar_vehiculo_trabajo_pesado(self):
        self.tipo_trabajo = "Vehiculo de trabajo pesado"