from Vehiculos_padre import Vehiculos
from deportivo_hijo import Deportivo_hijo

# +++++++vcodigo principal ++++++++
obj_vehiculo_padre = Vehiculos()
obj_vehiculo_padre.arranque(modelo, color, motor,numero_puertas, capacidad_pasajeros, tipo_combustible, dato_techo)

obj_hijo = Deportivo_hijo()
obj_hijo.arranque()


