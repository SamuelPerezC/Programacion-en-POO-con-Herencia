# botella_padre.py
class Botella:
    def __init__(self, material, capacidad, forma, diseño, tapa, grabados):
        # Atributos
        self.material = material
        self.capacidad = capacidad  # en ml
        self.forma = forma
        self.diseño = diseño
        self.tapa = tapa
        self.grabados = grabados
        self.liquido_actual = 0
        self.cerrada = True
    
    # Métodos
    def contener_liquidos(self, cantidad):
        if cantidad <= self.capacidad:
            self.liquido_actual = cantidad
            return f"✅ Conteniendo {cantidad}ml de líquido"
        else:
            return f"❌ Excede la capacidad de {self.capacidad}ml"
    
    def facilitar_vertido(self):
        if not self.cerrada and self.liquido_actual > 0:
            self.liquido_actual -= 50  # Simula vertido
            return f"🍶 Vertido facilitado. Liquido restante: {self.liquido_actual}ml"
        return "❌ No se puede verter (cerrada o vacía)"
    
    def cierre_hermetico(self, estado):
        self.cerrada = estado
        accion = "cerrada" if estado else "abierta"
        return f"🔒 Botella {accion} herméticamente"
    
    def transporte(self):
        if self.cerrada:
            return f"🚗 Transporte seguro de {self.capacidad}ml"
        return "⚠️ Cierra la botella antes del transporte"
    
    def manejo(self):
        peso_aprox = self.capacidad / 1000  # Simula peso en kg
        return f"👌 Manejo ergonómico. Peso aproximado: {peso_aprox}kg"
    
    def compatibilidad_bebidas(self, temperatura):
        if temperatura == "caliente":
            return "♨️ Compatible con bebidas calientes"
        elif temperatura == "fria":
            return "❄️ Compatible con bebidas frías"
        else:
            return "🌡 Compatible con bebidas a temperatura ambiente"
    
    def reutilizacion(self, veces_usada):
        return f"♻️ Botella reutilizable. Usada {veces_usada} veces"
    
    def transparencia(self, nivel):
        niveles = {1: "Opaca", 2: "Translúcida", 3: "Transparente"}
        return f"👀 Nivel de transparencia: {niveles.get(nivel, 'Desconocido')}"
    
    def mostrar_info(self):
        return f"""
=== INFORMACIÓN DE LA BOTELLA ===
Material: {self.material}
Capacidad: {self.capacidad}ml
Forma: {self.forma}
Diseño: {self.diseño}
Tapa: {self.tapa}
Grabados: {self.grabados}
Líquido actual: {self.liquido_actual}ml
Estado: {'Cerrada' if self.cerrada else 'Abierta'}
        """