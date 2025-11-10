from Botella import Botella

class Botella_Plastico(Botella):
    def __init__(self, capacidad, forma, diseño, tapa, grabados):
        # Siempre define material como "plastico" automáticamente
        super().__init__("plastico", capacidad, forma, diseño, tapa, grabados)

    # SOBREESCRITURA DE MÉTODOS con comportamiento específico del plástico:
    
    def reutilizacion(self):
        print("Puede reutilizarse pocas veces por seguridad sanitaria.")  # Limitaciones sanitarias

    def transparencia(self):
        print("El plástico es semitransparente y permite ver el contenido claramente.")  # Transparencia media

    def compatibilidad_bebidas(self):
        print("Ideal para bebidas frías, no recomendada para líquidos calientes.")  # Limitación térmica

    def manejo(self):
        print("Ligera y resistente a golpes, fácil de manejar.")  # Ventajas de durabilidad

    def mostrar_atributos(self):
        print(f"Material: plástico - Capacidad: {self.capacidad} - Forma: {self.forma} - Diseño: {self.diseño} - Tapa: {self.tapa} - Grabados: {self.grabados}")