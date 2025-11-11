class Base_datos:
    def __init__(self):
        """
        Inicializa el sistema de base de datos para animales
        Crea una lista vacía para almacenar instancias de animales
        """
        self.lista_animales = []  # Lista principal para almacenar animales

    def agregar_animal(self, animal):
        """
        Agrega un animal individual a la base de datos
        Parámetros:
            animal: Instancia de cualquier clase Animales
        """
        self.lista_animales.append(animal)  # Añade el objeto a la lista
        print(f"Animal '{animal.nombre}' agregado exitosamente.")

    def extender_lista(self, animales):
        """
        Agrega múltiples animales a la vez
        Parámetros:
            animales: Lista de instancias de animales
        """
        self.lista_animales.extend(animales)  # Extiende la lista con nuevos elementos
        print(f"Se agregaron {len(animales)} animales a la base de datos.")

    def eliminar_por_indice(self, indice):
        """
        Elimina un animal por su posición en la lista
        Parámetros:
            indice: Posición del animal a eliminar (0-based)
        Retorna:
            Animal eliminado o None si el índice es inválido
        """
        if 0 <= indice < len(self.lista_animales):
            animal_eliminado = self.lista_animales.pop(indice)  # Remueve y retorna el elemento
            print(f"Animal '{animal_eliminado.nombre}' eliminado.")
            return animal_eliminado
        print("Índice inválido. No se pudo eliminar el animal.")
        return None

    def copiar_lista(self):
        """
        Crea una copia de seguridad de la lista de animales
        Retorna:
            Copia de la lista actual de animales
        """
        return self.lista_animales.copy()  # Retorna una copia superficial de la lista

    def limpiar_lista(self):
        """Elimina todos los animales de la base de datos"""
        numero_animales = len(self.lista_animales)
        self.lista_animales.clear()  # Vacía completamente la lista
        print(f"Se eliminaron {numero_animales} animales de la base de datos.")

    def invertir_lista(self):
        """Invierte el orden de los animales en la lista"""
        self.lista_animales.reverse()  # Modifica el orden interno de la lista
        print("Orden de la lista invertido.")

    def imprimir_info(self, filtro_tipo=None):
        """
        Muestra información de los animales con filtro opcional
        Parámetros:
            filtro_tipo: Tipo específico de animal a filtrar
        """
        lista_filtrada = self.lista_animales
        
        # Aplica filtro si se especifica
        if filtro_tipo:
            lista_filtrada = [animal for animal in self.lista_animales 
                            if animal.__class__.__name__.lower() == filtro_tipo.lower()]
        
        # Verifica si hay animales para mostrar
        if not lista_filtrada:
            print("No hay animales para mostrar con ese filtro.")
            return

        # Muestra información de cada animal
        print(f"\n--- Mostrando {len(lista_filtrada)} animal(es) ---")
        for i, animal in enumerate(lista_filtrada):
            print(f"{i}. ", end="")
            animal.mostrar_atributos()  # Llama al método del objeto específico

    def contar_animales_por_tipo(self):
        """
        Cuenta y muestra estadísticas por tipo de animal
        """
        if not self.lista_animales:
            print("No hay animales en la base de datos.")
            return
            
        contador = {}
        for animal in self.lista_animales:
            tipo = animal.__class__.__name__
            contador[tipo] = contador.get(tipo, 0) + 1
        
        print("\n--- Estadísticas por Tipo ---")
        for tipo, cantidad in contador.items():
            print(f"{tipo}: {cantidad} animal(es)")
