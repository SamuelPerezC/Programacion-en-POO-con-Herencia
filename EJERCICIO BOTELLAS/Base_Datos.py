class Base_datos:
    def __init__(self):
        self.lista_botellas = []  # Almacena todas las botellas del sistema

    # Agrega una botella individual a la lista
    def agregar_botella(self, botella):
        self.lista_botellas.append(botella)

    # Agrega múltiples botellas a la vez
    def extender_lista(self, botellas):
        self.lista_botellas.extend(botellas)

    # Elimina una botella por su posición en la lista
    def eliminar_por_indice(self, indice):
        if 0 <= indice < len(self.lista_botellas):
            return self.lista_botellas.pop(indice)
        return None
    
    # Crea una copia de seguridad de la lista
    def copiar_lista(self):
        return self.lista_botellas.copy()

    # Vacía toda la lista de botellas
    def limpiar_lista(self):
        self.lista_botellas.clear()

    # Invierte el orden de la lista
    def invertir_lista(self):
        self.lista_botellas.reverse()

    # Muestra información de botellas con filtro opcional por material
    def imprimir_info(self, filtro_material=None):
        lista = self.lista_botellas
        # Filtra por material si se especifica
        if filtro_material:
            lista = [b for b in lista if b.material.lower() == filtro_material.lower()]

        if not lista:
            print("No hay botellas para mostrar con ese filtro.")
            return

        # Muestra todas las botellas con numeración
        for i, botella in enumerate(lista):
            print(f"{i}. ", end="")
            botella.mostrar_atributos()