class Usuario:
    def __init__(self,nombre, direccion, correo)
    self.nombre=nombre
    self.direccion=direccion
    self.correo=correo
    self.lista_tarea=[]

    def  validar_usuario(self):
        return "usuario validado"

    def __str__(self):
         return f"nombre: {self.nombre} - direccion: {self.direccion} - correo: {self.correo}"

    def asignar_tarea(self,objeto_tarea):
        self.lista_tarea.append(objeto_tarea)
        print(objeto_tarea)