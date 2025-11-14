from animal_equino import animal_equino
from animal_cocodrilo import animal_cocodrilo
from animal_insecto import animal_insecto
from Animales import Animales
from Base_Datos import Base_datos

bd = Base_datos()

def menu_principal():
    print("\n--- MENÚ ANIMALES ---")
    print("1. Crear animal equino")
    print("2. Crear animal cocodrilo")
    print("3. Crear animal insecto")
    print("4. Crear animal normal")
    print("5. Ver listas")
    print("6. Eliminar un animal")
    print("7. Salir")
    return input("Elige una opción: ")

def menu_ver_listas():
    print("\n--- VER LISTAS ---")
    print("1. Ver todos los animales")
    print("2. Ver solo animales equinos")
    print("3. Ver solo animales cocodrilo")
    print("4. Ver solo animales insecto")
    print("5. Ver solo animales normales")
    print("6. Volver al menú principal")
    return input("Elige una opción: ")

def crear_animal_equino():
    nombre = input("Nombre: ") 
    edad = input("Edad: ") 
    habitad = input("Hábitat: ") 
    dieta = input("Dieta: ") 
    tamaño = input("Tamaño: ") 
    color = input("Color: ") 
    
    animal_equino_obj = animal_equino(nombre, edad, habitad, dieta, tamaño, color)
    bd.agregar_animal(animal_equino_obj)
    print("Animal equino creado y registrado.")
    animal_equino_obj.moverse()
    animal_equino_obj.comunicacion()
    animal_equino_obj.descanso()

def crear_animal_cocodrilo():
    nombre = input("Nombre: ") 
    edad = input("Edad: ") 
    habitad = input("Hábitat: ") 
    dieta = input("Dieta: ") 
    tamaño = input("Tamaño: ") 
    color = input("Color: ")
    
    animal_cocodrilo_obj = animal_cocodrilo(nombre, edad, habitad, dieta, tamaño, color)
    bd.agregar_animal(animal_cocodrilo_obj)
    print("Animal cocodrilo creado y registrado.")
    animal_cocodrilo_obj.moverse()
    animal_cocodrilo_obj.instintos()
    animal_cocodrilo_obj.sueño()

def crear_animal_insecto():
    nombre = input("Nombre: ") 
    edad = input("Edad: ") 
    habitad = input("Hábitat: ") 
    dieta = input("Dieta: ") 
    tamaño = input("Tamaño: ") 
    color = input("Color: ")
    
    animal_insecto_obj = animal_insecto(nombre, edad, habitad, dieta, tamaño, color)
    bd.agregar_animal(animal_insecto_obj)
    print("Animal insecto creado y registrado.")
    animal_insecto_obj.moverse()
    animal_insecto_obj.adaptacion()
    animal_insecto_obj.interaccion_social()

def crear_animal_normal():
    nombre = input("Nombre: ") 
    edad = input("Edad: ") 
    habitad = input("Hábitat: ") 
    dieta = input("Dieta: ") 
    tamaño = input("Tamaño: ") 
    color = input("Color: ")
    
    animal_normal = Animales(nombre, edad, habitad, dieta, tamaño, color)
    bd.agregar_animal(animal_normal)
    print("Animal normal creado y registrado.")
    animal_normal.moverse()
    animal_normal.comunicacion()
    animal_normal.reproduccion()

def ver_listas():
    while True:
        opcion = menu_ver_listas()
        if opcion == "1":
            print("\n--- Todos los animales ---")
            bd.imprimir_info()
        elif opcion == "2":
            print("\n--- Animales equinos ---")
            bd.imprimir_info(filtro_tipo="animal_equino")
        elif opcion == "3":
            print("\n--- Animales cocodrilo ---")
            bd.imprimir_info(filtro_tipo="animal_cocodrilo")
        elif opcion == "4":
            print("\n--- Animales insecto ---")
            bd.imprimir_info(filtro_tipo="animal_insecto")
        elif opcion == "5":
            print("\n--- Animales normales ---")
            lista = [a for a in bd.lista_animales if a.__class__.__name__ == "Animales"]
            if not lista:
                print("No hay animales de ese tipo.")
            else:
                for i, animal in enumerate(lista):
                    print(f"{i}. ", end="")
                    animal.mostrar_atributos()
        elif opcion == "6":
            break
        else:
            print("Opción no válida en Ver listas.")

def eliminar_animal():
    if not bd.lista_animales:
        print("No hay animales para eliminar.")
        return
    print("\n--- Eliminar animal ---")
    for i, animal in enumerate(bd.lista_animales):
        print(f"{i}. ", end="")
        animal.mostrar_atributos()
    try:
        indice = int(input("Ingresa el número del animal que deseas eliminar: "))
        if 0 <= indice < len(bd.lista_animales):
            eliminada = bd.eliminar_por_indice(indice)
            print(f"Animal eliminado")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor ingresa un número válido.")

def main():
    while True:
        opcion = menu_principal()
        if opcion == "1":
            crear_animal_equino()
        elif opcion == "2":
            crear_animal_cocodrilo()
        elif opcion == "3":
            crear_animal_insecto()
        elif opcion == "4":
            crear_animal_normal()
        elif opcion == "5":
            ver_listas()
        elif opcion == "6":
            eliminar_animal()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()