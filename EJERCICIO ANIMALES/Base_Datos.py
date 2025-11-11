class Base_datos:
    def __init__(self):
        self.lista_animales = []

    def agregar_animales(self, Animales):
        self.lista_animales.append(Animales)

    def extender_lista(self, Animales):
        self.lista_Animales.extend(Animales)

    def eliminar_por_indice(self, indice):
        if 0 <= indice < len(self.lista_Animales):
            return self.lista_Animales.pop(indice)
        return None

    def copiar_lista(self):
        return self.lista_Animales.copy()

    def limpiar_lista(self):
        self.lista_Animales.clear()

    def invertir_lista(self):
        self.lista_Animales.reverse()

    def imprimir_info(self, filtro_tipo=None):
        lista = self.lista_Animales
        if filtro_tipo:
            lista = [v for v in lista if v.__class__.__name__.lower() == filtro_tipo.lower()]

        if not lista:
            print("No hay animales para mostrar con ese filtro.")
            return

        for i, Animales in enumerate(lista):
            print(f"{i}. ", end="")
            Animales.mostrar_atributos()