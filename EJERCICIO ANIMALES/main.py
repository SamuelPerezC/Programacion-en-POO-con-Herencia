from animal_equino import animal_equino
from animal_cocodrilo import animal_cocodrilo
from animal_insecto import animal_insecto
from animal_pez import animal_pez
from animal_pato import Animal_pato
from Animales import Animales
from Base_Datos import Base_datos

# Instancia global de la base de datos
bd = Base_datos()

def menu_principal():
    """
    Muestra el menú principal del sistema de animales
    Retorna:
        Opción seleccionada por el usuario
    """
    print("\n" + "="*50)
    print("          SISTEMA DE GESTIÓN DE ANIMALES")
    print("="*50)
    print("1. 🐎 Crear animal equino")
    print("2. 🐊 Crear animal cocodrilo") 
    print("3. 🐜 Crear animal insecto")
    print("4. 🐠 Crear animal pez")
    print("5. 🦆 Crear animal pato")
    print("6. 🐾 Crear animal normal")
    print("7. 👁️ Ver animales")
    print("8. 🗑️ Eliminar animal")
    print("9. 📊 Estadísticas")
    print("10. ❌ Salir")
    print("-"*50)
    return input("Selecciona una opción (1-10): ")

def menu_ver_animales():
    """
    Submenú para visualizar animales con diferentes filtros
    Retorna:
        Opción de visualización seleccionada
    """
    print("\n--- VISUALIZAR ANIMALES ---")
    print("1. 👁️ Ver todos los animales")
    print("2. 🐎 Ver solo equinos")
    print("3. 🐊 Ver solo cocodrilos")
    print("4. 🐜 Ver solo insectos")
    print("5. 🐠 Ver solo peces")
    print("6. 🦆 Ver solo patos")
    print("7. 🐾 Ver solo animales normales")
    print("8. ↩️ Volver al menú principal")
    return input("Selecciona una opción (1-8): ")

def solicitar_datos_animal():
    """
    Solicita datos básicos comunes a todos los animales
    Retorna:
        Tupla con los datos del animal
    """
    print("\n--- INGRESO DE DATOS DEL ANIMAL ---")
    nombre = input("Nombre del animal: ")
    edad = input("Edad del animal: ")
    habitad = input("Hábitat natural: ")
    dieta = input("Tipo de dieta: ")
    tamaño = input("Tamaño del animal: ")
    color = input("Color predominante: ")
    return nombre, edad, habitad, dieta, tamaño, color

def crear_animal_equino():
    """Crea y registra un animal equino en el sistema"""
    print("\n--- CREANDO ANIMAL EQUINO ---")
    datos = solicitar_datos_animal()
    equino = animal_equino(*datos)
    bd.agregar_animal(equino)
    
    # Demostración de comportamientos específicos
    print("\n--- COMPORTAMIENTOS EQUINO ---")
    equino.moverse()
    equino.comunicacion()
    equino.descanso()
    print("✅ Animal equino creado exitosamente!")

def crear_animal_cocodrilo():
    """Crea y registra un cocodrilo en el sistema"""
    print("\n--- CREANDO COCODRILO ---")
    datos = solicitar_datos_animal()
    cocodrilo = animal_cocodrilo(*datos)
    bd.agregar_animal(cocodrilo)
    
    print("\n--- COMPORTAMIENTOS COCODRILO ---")
    cocodrilo.moverse()
    cocodrilo.instintos()
    cocodrilo.sueño()
    print("✅ Cocodrilo creado exitosamente!")

def crear_animal_insecto():
    """Crea y registra un insecto en el sistema"""
    print("\n--- CREANDO INSECTO ---")
    datos = solicitar_datos_animal()
    insecto = animal_insecto(*datos)
    bd.agregar_animal(insecto)
    
    print("\n--- COMPORTAMIENTOS INSECTO ---")
    insecto.moverse()
    insecto.adaptacion()
    insecto.interaccion_social()
    print("✅ Insecto creado exitosamente!")

def crear_animal_pez():
    """Crea y registra un pez en el sistema"""
    print("\n--- CREANDO PEZ ---")
    datos = solicitar_datos_animal()
    pez = animal_pez(*datos)
    bd.agregar_animal(pez)
    
    print("\n--- COMPORTAMIENTOS PEZ ---")
    pez.moverse()
    pez.comunicacion()
    pez.descanso()
    
    # Comportamientos adicionales específicos de peces
    if hasattr(pez, 'respirar_agua'):
        pez.respirar_agua()
    print("✅ Pez creado exitosamente!")

def crear_animal_pato():
    """Crea y registra un pato en el sistema"""
    print("\n--- CREANDO PATO ---")
    datos = solicitar_datos_animal()
    pato = Animal_pato(*datos)
    bd.agregar_animal(pato)
    
    print("\n--- COMPORTAMIENTOS PATO ---")
    pato.moverse()
    pato.adaptacion()
    pato.interaccion_social()
    
    # Comportamientos adicionales específicos de patos
    if hasattr(pato, 'bucear'):
        pato.bucear()
    if hasattr(pato, 'acicalarse'):
        pato.acicalarse()
    print("✅ Pato creado exitosamente!")

def crear_animal_normal():
    """Crea y registra un animal genérico en el sistema"""
    print("\n--- CREANDO ANIMAL NORMAL ---")
    datos = solicitar_datos_animal()
    animal = Animales(*datos)
    bd.agregar_animal(animal)
    
    print("\n--- COMPORTAMIENTOS GENÉRICOS ---")
    animal.moverse()
    animal.comunicacion()
    animal.reproduccion()
    print("✅ Animal normal creado exitosamente!")

def ver_animales():
    """Sistema de navegación para visualizar animales"""
    while True:
        opcion = menu_ver_animales()
        if opcion == "1":
            print("\n--- TODOS LOS ANIMALES ---")
            bd.imprimir_info()
        elif opcion == "2":
            print("\n--- ANIMALES EQUINOS ---")
            bd.imprimir_info(filtro_tipo="animal_equino")
        elif opcion == "3":
            print("\n--- COCODRILOS ---")
            bd.imprimir_info(filtro_tipo="animal_cocodrilo")
        elif opcion == "4":
            print("\n--- INSECTOS ---")
            bd.imprimir_info(filtro_tipo="animal_insecto")
        elif opcion == "5":
            print("\n--- PECES ---")
            bd.imprimir_info(filtro_tipo="animal_pez")
        elif opcion == "6":
            print("\n--- PATOS ---")
            bd.imprimir_info(filtro_tipo="Animal_pato")
        elif opcion == "7":
            print("\n--- ANIMALES NORMALES ---")
            bd.imprimir_info(filtro_tipo="Animales")
        elif opcion == "8":
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.")

def eliminar_animal():
    """Sistema de eliminación de animales con validación"""
    if not bd.lista_animales:
        print("❌ No hay animales para eliminar.")
        return
        
    print("\n--- ELIMINAR ANIMAL ---")
    print("Animales registrados:")
    bd.imprimir_info()  # Muestra todos los animales numerados
    
    try:
        indice = int(input("\nIngresa el número del animal a eliminar: "))
        resultado = bd.eliminar_por_indice(indice)
        if resultado:
            print(f"✅ Animal eliminado correctamente.")
        else:
            print("❌ No se pudo eliminar el animal.")
    except ValueError:
        print("❌ Error: Debes ingresar un número válido.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

def mostrar_estadisticas():
    """Muestra estadísticas del sistema"""
    print("\n--- ESTADÍSTICAS DEL SISTEMA ---")
    bd.contar_animales_por_tipo()
    
    # Información adicional
    total_animales = len(bd.lista_animales)
    print(f"\n📈 Total de animales registrados: {total_animales}")
    
    if total_animales > 0:
        print("🎯 Sistema funcionando correctamente")
    else:
        print("ℹ️  El sistema está vacío, agrega algunos animales")

def mostrar_bienvenida():
    """Muestra mensaje de bienvenida"""
    print("🐾" * 20)
    print("   BIENVENIDO AL SISTEMA DE GESTIÓN DE ANIMALES")
    print("🐾" * 20)
    print("Sistema desarrollado para gestionar diferentes tipos de animales")
    print("Puedes crear, visualizar, eliminar y obtener estadísticas")
    print("")

def main():
    """
    Función principal que controla el flujo del programa
    Bucle infinito hasta que el usuario elija salir
    """
    mostrar_bienvenida()
    
    while True:
        try:
            opcion = menu_principal()
            
            if opcion == "1":
                crear_animal_equino()
            elif opcion == "2":
                crear_animal_cocodrilo()
            elif opcion == "3":
                crear_animal_insecto()
            elif opcion == "4":
                crear_animal_pez()
            elif opcion == "5":
                crear_animal_pato()
            elif opcion == "6":
                crear_animal_normal()
            elif opcion == "7":
                ver_animales()
            elif opcion == "8":
                eliminar_animal()
            elif opcion == "9":
                mostrar_estadisticas()
            elif opcion == "10":
                print("\n" + "="*50)
                print("¡Gracias por usar el Sistema de Gestión de Animales! 🐅")
                print("Saliendo del programa...")
                print("="*50)
                break
            else:
                print("❌ Opción no válida. Por favor selecciona 1-10.")
                
        except KeyboardInterrupt:
            print("\n\n⚠️  Programa interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            print("💡 El sistema continuará funcionando...")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
