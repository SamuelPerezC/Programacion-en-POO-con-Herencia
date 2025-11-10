from botella_plastico import Botella_Plastico
from botella_vidrio import Botella_Vidrio
from Botella import Botella
from Base_Datos import Base_datos

# Instancia global de la base de datos
bd = Base_datos()

def menu_principal():
    # Menú principal con todas las opciones del sistema
    print("\n--- MENÚ BOTELLAS ---")
    print("1. Crear botella de plástico")
    print("2. Crear botella de vidrio") 
    print("3. Crear botella normal")
    print("4. Ver listas")
    print("5. Eliminar una botella")
    print("6. Salir")
    return input("Elige una opción: ")

def menu_ver_listas():
    # Submenú para diferentes vistas de los datos
    print("\n--- VER LISTAS ---")
    print("1. Ver todas las botellas")
    print("2. Ver solo botellas de plástico")
    print("3. Ver solo botellas de vidrio")
    print("4. Ver solo botellas 'normales' (material distinto)")
    print("5. Volver al menú principal")
    return input("Elige una opción: ")

def crear_botella_plastico():
    # Captura datos y crea botella de plástico con validaciones específicas
    capacidad = input("Capacidad (ej: 1L): ") 
    forma = input("Forma (ej: Cilíndrica): ") 
    diseño = input("Diseño: ") 
    tapa = input("Tapa: ") 
    grabados = input("Grabados: ") 
    
    botella_plastico = Botella_Plastico(capacidad, forma, diseño, tapa, grabados)
    bd.agregar_botella(botella_plastico)
    print("Botella de plástico creada y registrada.")
    
    # Demostración de funcionalidades específicas
    botella_plastico.contener_liquidos()
    botella_plastico.transparencia()
    botella_plastico.reutilizacion()
    botella_plastico.compatibilidad_bebidas()

def crear_botella_vidrio():
    # Similar a plástico pero con características de vidrio
    capacidad = input("Capacidad (ej: 750ml): ") 
    forma = input("Forma (ej: Recta): ") 
    diseño = input("Diseño: ") 
    tapa = input("Tapa: ")
    grabados = input("Grabados: ") 
    
    botella_vidrio = Botella_Vidrio(capacidad, forma, diseño, tapa, grabados)
    bd.agregar_botella(botella_vidrio)
    print("Botella de vidrio creada y registrada.")
    
    botella_vidrio.contener_liquidos()
    botella_vidrio.compatibilidad_bebidas()
    botella_vidrio.manejo()
    botella_vidrio.transparencia()

def crear_botella_normal():
    # Para materiales distintos a plástico y vidrio
    material = input("Material (ej: metal, cartón, normal): ") 
    capacidad = input("Capacidad (ej: 2L): ") 
    forma = input("Forma: ") 
    diseño = input("Diseño: ") 
    tapa = input("Tapa: ") 
    grabados = input("Grabados: ") 
    
    botella_normal = Botella(material, capacidad, forma, diseño, tapa, grabados)
    bd.agregar_botella(botella_normal)
    print("Botella normal creada y registrada.")
    
    botella_normal.contener_liquidos()
    botella_normal.transporte()
    botella_normal.reutilizacion()     
    botella_normal.cierre_hermetico()
    botella_normal.compatibilidad_bebidas()

def ver_listas():
    # Sistema de navegación para ver diferentes categorías
    while True:
        opcion = menu_ver_listas()
        if opcion == "1":
            print("\n--- Todas las botellas ---")
            bd.imprimir_info()
        elif opcion == "2":
            print("\n--- Botellas de plástico ---")
            bd.imprimir_info(filtro_material="plastico")
        elif opcion == "3":
            print("\n--- Botellas de vidrio ---")
            bd.imprimir_info(filtro_material="vidrio")
        elif opcion == "4":
            print("\n--- Botellas 'normales' (no plástico ni vidrio) ---")
            # Filtro personalizado para materiales excluidos
            lista = [b for b in bd.lista_botellas if b.material.lower() not in ("plastico", "vidrio")]
            if not lista:
                print("No hay botellas de ese tipo.")
            else:
                for i, botella in enumerate(lista):
                    print(f"{i}. ", end="")
                    botella.mostrar_atributos()
        elif opcion == "5":
            break
        else:
            print("Opción no válida en Ver listas.")

def eliminar_botella():
    # Sistema de eliminación con validación de índices
    if not bd.lista_botellas:
        print("No hay botellas para eliminar.")
        return
        
    print("\n--- Eliminar botella ---")
    # Muestra todas las botellas numeradas
    for i, botella in enumerate(bd.lista_botellas):
        print(f"{i}. ", end="")
        botella.mostrar_atributos()
        
    try:
        indice = int(input("Ingresa el número de la botella que deseas eliminar: "))
        if 0 <= indice < len(bd.lista_botellas):
            eliminada = bd.eliminar_por_indice(indice)
            print(f"Botella eliminada")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor ingresa un número válido.")

def main():
    # Bucle principal del programa
    while True:
        opcion = menu_principal()
        if opcion == "1":
            crear_botella_plastico()
        elif opcion == "2":
            crear_botella_vidrio()
        elif opcion == "3":
            crear_botella_normal()
        elif opcion == "4":
            ver_listas()
        elif opcion == "5":
            eliminar_botella()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()