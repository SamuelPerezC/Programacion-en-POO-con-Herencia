# main.py
from botella_plastico import BotellaPlastico
from botella_vidrio import BotellaVidrio

def demostrar_botellas():
    print("🚰 DEMOSTRACIÓN DE BOTELLAS 🚰\n")
    
    # Crear botellas
    botella_plastico = BotellaPlastico(
        capacidad=500,
        forma="Cilíndrica",
        diseño="Deportivo",
        tapa="Rosca",
        grabados="Logo marca",
        tipo_plastico="PET",
        reciclable=True
    )
    
    botella_vidrio = BotellaVidrio(
        capacidad=750,
        forma="Elegante",
        diseño="Clásico",
        tapa="Corcho",
        grabados="Grabado artístico",
        tipo_vidrio="borosilicato",
        espesor=3
    )
    
    # Probar métodos de botella plástico
    print("=== BOTELLA DE PLÁSTICO ===")
    print(botella_plastico.mostrar_info())
    print(botella_plastico.info_especifica())
    print(botella_plastico.contener_liquidos(400))
    print(botella_plastico.cierre_hermetico(False))
    print(botella_plastico.facilitar_vertido())
    print(botella_plastico.peso_ligero())
    print(botella_plastico.resistencia_caidas())
    print(botella_plastico.compatibilidad_bebidas("caliente"))
    print(botella_plastico.reutilizacion(15))
    print(botella_plastico.transparencia(3))
    
    print("\n" + "="*50 + "\n")
    
    # Probar métodos de botella vidrio
    print("=== BOTELLA DE VIDRIO ===")
    print(botella_vidrio.mostrar_info())
    print(botella_vidrio.info_especifica())
    print(botella_vidrio.contener_liquidos(600))
    print(botella_vidrio.preservar_sabor())
    print(botella_vidrio.resistencia_termica())
    print(botella_vidrio.manejo())
    print(botella_vidrio.transporte())
    print(botella_vidrio.compatibilidad_bebidas("caliente"))
    print(botella_vidrio.reutilizacion(100))
    print(botella_vidrio.transparencia(3))

def menu_interactivo():
    print("\n" + "="*60)
    print("🎯 MENÚ INTERACTIVO - SISTEMA DE BOTELLAS")
    print("="*60)
    
    # Crear algunas botellas para el menú
    botellas = [
        BotellaPlastico(1000, "Rectangular", "Moderno", "Tapón", "Rayas", "HDPE", True),
        BotellaVidrio(500, "Redonda", "Vintage", "Tapón de madera", "Flores", "templado", 2)
    ]
    
    while True:
        print("\nOpciones:")
        print("1. Mostrar información de todas las botellas")
        print("2. Probar métodos de botella plástico")
        print("3. Probar métodos de botella vidrio")
        print("4. Salir")
        
        opcion = input("\nSelecciona una opción (1-4): ")
        
        if opcion == "1":
            for i, botella in enumerate(botellas, 1):
                print(f"\n--- Botella {i} ---")
                print(botella.mostrar_info())
                
        elif opcion == "2":
            plastico = botellas[0]
            print("\n🔵 PROBANDO BOTELLA PLÁSTICO:")
            print(plastico.contener_liquidos(800))
            print(plastico.peso_ligero())
            print(plastico.resistencia_caidas())
            
        elif opcion == "3":
            vidrio = botellas[1]
            print("\n🟢 PROBANDO BOTELLA VIDRIO:")
            print(vidrio.contener_liquidos(400))
            print(vidrio.preservar_sabor())
            print(vidrio.resistencia_termica())
            
        elif opcion == "4":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

# Ejecutar programa
if __name__ == "__main__":
    demostrar_botellas()
    menu_interactivo()