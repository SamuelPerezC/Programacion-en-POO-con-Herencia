from usuario import Usuario
from Base_datos import Base_datos

objeto_tarea = Tareas("Codigo1", "Estudiar Matematicas")
objeto_usuario = Usuario ("Pepito","Sena","Sena.edu.co")
objeto_usuario.asignar_tarea(objeto_tarea)
print(objeto_tarea)

objeto_base_datos = Base_datos()
objeto_base_datos.guardar_informacion(objeto_usuario)
print(objeto_base_datos)

objeto_base_datos.imprimir_informacion()

datos= objeto_usuario.validar_usuario()
print(datos)

objeto_usuario.eliminar_tarea("estudiar matematicas")

objeto_base_datos.lista_informacion

