# botella_plastico.py
from botella_padre import Botella

class BotellaPlastico(Botella):
    def __init__(self, capacidad, forma, diseño, tapa, grabados, tipo_plastico, reciclable):
        super().__init__("Plástico", capacidad, forma, diseño, tapa, grabados)
        # Atributos específicos de plástico
        self.tipo_plastico = tipo_plastico  # PET, HDPE, etc.
        self.reciclable = reciclable
        self.flexible = True
    
    # Métodos específicos para plástico
    def resistencia_caidas(self):
        return "💪 Alta resistencia a caídas y golpes"
    
    def peso_ligero(self):
        peso = self.capacidad * 0.0001  # Peso muy ligero
        return f"🪶 Peso muy ligero: {peso:.2f}kg"
    
    def compatibilidad_bebidas(self, temperatura):
        if temperatura == "caliente":
            return "⚠️ No recomendada para bebidas muy calientes"
        return super().compatibilidad_bebidas(temperatura)
    
    def reutilizacion(self, veces_usada):
        vida_util = 50 - veces_usada
        if vida_util > 0:
            return f"♻️ Botella plástica. Vida útil restante: {vida_util} usos"
        return "⏹️ Botella plástica llegó al fin de su vida útil"
    
    def info_especifica(self):
        return f"""
=== BOTELLA DE PLÁSTICO ===
Tipo de plástico: {self.tipo_plastico}
Reciclable: {'Sí' if self.reciclable else 'No'}
Flexible: {'Sí' if self.flexible else 'No'}
        """