class Base_datos:
    def __init__(self):
        self.lista_informacion = []  # Almacena todas las tareas del sistema

    def guardar_informacion(self, objeto_usuario):
        self.lista_informacion.append(objeto_usuario)

    def imprimir_informacion(self):
        for objeto_usuario in self.lista_informacion:
            print(objeto_usuario.nombre)
            for objeto_tarea in objeto_usuario.lista_tarea:
                print(objeto_tarea.descripcion)
        
        