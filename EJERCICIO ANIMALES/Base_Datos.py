class Base_datos:
    def __init__(self):
        self.lista_animales = []

    def agregar_animal(self, animal):
        self.lista_animales.append(animal)

    def extender_lista(self, animales):
        self.lista_animales.extend(animales)

    def eliminar_por_indice(self, indice):
        if 0 <= indice < len(self.lista_animales):
            return self.lista_animales.pop(indice)
        return None
    
    def copiar_lista(self):
        return self.lista_animales.copy()

    def limpiar_lista(self):
        self.lista_animales.clear()

    def invertir_lista(self):
        self.lista_animales.reverse()

    def imprimir_info(self, filtro_tipo=None):
        lista = self.lista_animales
        if filtro_tipo:
            lista = [a for a in lista if a.__class__.__name__.lower() == filtro_tipo.lower()]

        if not lista:
            print("No hay animales para mostrar con ese filtro.")
            return

        for i, animal in enumerate(lista):
            print(f"{i}. ", end="")
            animal.mostrar_atributos()