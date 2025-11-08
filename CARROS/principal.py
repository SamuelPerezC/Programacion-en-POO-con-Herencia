#principal.py
from Vehiculos_padre import Vehiculos
from deportivo_hijo import Deportivo_hijo
from chana_hijo import chana_hijo
from volqueta_hijo import volqueta_hijo

#================ codigo principal =========================
obj_vehiculo_padre = Vehiculos("Modelo Generico","Multicolor", "2.0L,",4,5,"Gasolina")
obj_vehiculo_padre.arranque()

obj_hijo = Deportivo_hijo("Ferrari","Negro", "4.0L,",2,2,"Premium", "Descapotado")
obj_hijo.arranque()
obj_hijo.activar_techo()

obj_hijo_chana = chana_hijo("Chana","Blanco","1600L",3,2,"Gasolina Corriente","Vehiculo especial para trabajo liviano")
obj_hijo_chana.arranque()
obj_hijo_chana.activar_vehiculo_trabajo()

obj_hijo_volqueta = volqueta_hijo("Piraña","Negro","5600",2,2,"Diesel","Vehiculo especial para Carga pesada")
obj_hijo_volqueta.arranque()
obj_hijo_volqueta.activar_vehiculo_trabajo_pesado()








