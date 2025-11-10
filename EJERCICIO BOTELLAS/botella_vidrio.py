from Botella import Botella

class Botella_Vidrio(Botella):
    def __init__(self, capacidad, forma, diseño, tapa, grabados):
        # Siempre define material como "vidrio" automáticamente
        super().__init__("vidrio", capacidad, forma, diseño, tapa, grabados)

    # SOBREESCRITURA DE MÉTODOS con comportamiento específico del vidrio:
    
    def reutilizacion(self):
        print("Puede reutilizarse muchas veces, es más resistente y ecológica.")  # Ventaja ecológica

    def compatibilidad_bebidas(self):
        print("Puede contener bebidas calientes o frías sin deformarse ni alterar el sabor.")  # Versatilidad térmica

    def transparencia(self):
        print("Totalmente transparente, permite ver el contenido perfectamente.")  # Máxima transparencia

    def manejo(self):
        print("Requiere cuidado en el manejo por su fragilidad.")  # Desventaja de fragilidad

    def transporte(self):
        print("Transporte seguro recomendado con protección adicional.")  # Precauciones especiales

    def mostrar_atributos(self):
        print(f"Material: vidrio - Capacidad: {self.capacidad} - Forma: {self.forma} - Diseño: {self.diseño} - Tapa: {self.tapa} - Grabados: {self.grabados}")