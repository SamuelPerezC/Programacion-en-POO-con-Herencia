class Base_datos:
    def __init__(self):
        self.lista_vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.lista_vehiculos.append(vehiculo)

    def extender_lista(self, vehiculos):
        self.lista_vehiculos.extend(vehiculos)

    def eliminar_por_indice(self, indice):
        if 0 <= indice < len(self.lista_vehiculos):
            return self.lista_vehiculos.pop(indice)
        return None
    
    def copiar_lista(self):
        return self.lista_vehiculos.copy()

    def limpiar_lista(self):
        self.lista_vehiculos.clear()

    def invertir_lista(self):
        self.lista_vehiculos.reverse()

    def imprimir_info(self, filtro_tipo=None):
        lista = self.lista_vehiculos
        if filtro_tipo:
            lista = [v for v in lista if v.__class__.__name__.lower() == filtro_tipo.lower()]

        if not lista:
            print("No hay vehículos para mostrar con ese filtro.")
            return

        for i, vehiculo in enumerate(lista):
            print(f"{i}. ", end="")
            vehiculo.mostrar_atributos()