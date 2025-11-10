class Botella:
    def __init__(self, material, capacidad, forma, diseño, tapa, grabados):
        # Atributos fundamentales de cualquier botella
        self.material = material    # Material de construcción
        self.capacidad = capacidad  # Volumen que contiene
        self.forma = forma          # Forma física
        self.diseño = diseño        # Estética y apariencia
        self.tapa = tapa           # Tipo de cierre
        self.grabados = grabados   # Decoraciones o marcas

    # MÉTODOS FUNCIONALES:
    
    def contener_liquidos(self):
        print("Contiene líquidos de manera segura.")  # Función básica

    def facil_vertido(self):
        print("Facilita el vertido del contenido.")   # Facilidad de uso

    def cierre_hermetico(self):
        print("Posee un cierre hermético.")          # Prevención de derrames

    def transporte(self):
        print("Permite el transporte de líquidos.")  # Portabilidad

    def manejo(self):
        print("Ofrece un manejo cómodo y seguro.")   # Ergonomía

    def compatibilidad_bebidas(self):
        print("Es compatible con diferentes tipos de bebidas.")  # Versatilidad

    def reutilizacion(self):
        print("Puede ser reutilizada.")              # Sostenibilidad

    def transparencia(self):
        print("Permite ver el contenido en cierta medida.")  # Visibilidad

    # Muestra todos los atributos en formato legible
    def mostrar_atributos(self):
        print(f"Material: {self.material} - Capacidad: {self.capacidad} - Forma: {self.forma} - Diseño: {self.diseño} - Tapa: {self.tapa} - Grabados: {self.grabados}")