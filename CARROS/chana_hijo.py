# chana_hijo.py
from Vehiculos_padre import Vehiculos

class chana_hijo(Vehiculos):
    def __init__(self, modelo, color, motor,numero_puertas, capacidad_pasajeros, tipo_combustible, dato_trabajo):
        super().__init__(modelo, color, motor,numero_puertas, capacidad_pasajeros, tipo_combustible)
        #Atributos para vehiculo deportivo
        self.tipo_trabajo_liviano = dato_trabajo
        
    def activar_vehiculo_trabajo(self):
        self.tipo_trabajo = "Vehiculo de trabajo liviano"