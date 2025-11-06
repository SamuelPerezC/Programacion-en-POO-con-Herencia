# botella_vidrio.py
from botella_padre import Botella

class BotellaVidrio(Botella):
    def __init__(self, capacidad, forma, diseño, tapa, grabados, tipo_vidrio, espesor):
        super().__init__("Vidrio", capacidad, forma, diseño, tapa, grabados)
        # Atributos específicos de vidrio
        self.tipo_vidrio = tipo_vidrio  # Borosilicato, templado, etc.
        self.espesor = espesor  # en mm
        self.fragil = True
    
    # Métodos específicos para vidrio
    def preservar_sabor(self):
        return "👅 Preserva el sabor original de las bebidas"
    
    def resistencia_termica(self):
        if self.tipo_vidrio == "borosilicato":
            return "🔥 Alta resistencia térmica (hasta 400°C)"
        else:
            return "🌡 Resistencia térmica moderada"
    
    def compatibilidad_bebidas(self, temperatura):
        if self.tipo_vidrio == "borosilicato":
            return "🔥♨️ Excelente para bebidas calientes y frías"
        return super().compatibilidad_bebidas(temperatura)
    
    def transparencia(self, nivel):
        if nivel == 3:
            return "💎 Transparencia cristalina máxima"
        return super().transparencia(nivel)
    
    def reutilizacion(self, veces_usada):
        return f"♻️ Botella de vidrio. Reutilizable indefinidamente. Usada {veces_usada} veces"
    
    def manejo(self):
        return "⚠️ Manejo con cuidado - Material frágil"
    
    def info_especifica(self):
        return f"""
=== BOTELLA DE VIDRIO ===
Tipo de vidrio: {self.tipo_vidrio}
Espesor: {self.espesor}mm
Frágil: {'Sí' if self.fragil else 'No'}
        """