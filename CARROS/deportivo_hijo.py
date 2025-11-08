# deportivo_hijo.py
from Vehiculos_padre import Vehiculos

class Deportivo_hijo(Vehiculos):
    def __init__(self, modelo, color, motor,numero_puertas, capacidad_pasajeros, tipo_combustible, dato_techo):
        super().__init__(modelo, color, motor,numero_puertas, capacidad_pasajeros, tipo_combustible)
        #Atributos para vehiculo deportivo
        self.tipo_techo = dato_techo
        
    def activar_techo(self):
        self.tipo_techo = "Techo activado"
        print(f"El techo ha sido activado: {self.tipo_techo}")
            
            
            
        
            
            
            
            

        
