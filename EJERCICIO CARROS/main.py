from carro_deportivo import Carro_Deportivo
from chana_furgon import Chana_Furgon
from volqueta import Volqueta
from Vehiculo import Vehiculo
from Base_Datos import Base_datos

bd = Base_datos()

def menu_principal():
    print("\n--- MENÚ VEHÍCULOS ---")
    print("1. Crear carro deportivo")
    print("2. Crear chana furgón")
    print("3. Crear volqueta")
    print("4. Crear vehículo normal")
    print("5. Ver listas")
    print("6. Eliminar un vehículo")
    print("7. Salir")
    return input("Elige una opción: ")

def menu_ver_listas():
    print("\n--- VER LISTAS ---")
    print("1. Ver todos los vehículos")
    print("2. Ver solo carros deportivos")
    print("3. Ver solo chana furgones")
    print("4. Ver solo volquetas")
    print("5. Ver solo vehículos normales")
    print("6. Volver al menú principal")
    return input("Elige una opción: ")

def crear_carro_deportivo():
    modelo = input("Modelo (ej: Ferrari 488): ") 
    color = input("Color (ej: Rojo): ") 
    motor = input("Motor (ej: V8 3.9L): ") 
    numero_puertas = input("Número de puertas: ") 
    capacidad_pasajeros = input("Capacidad de pasajeros: ") 
    tipo_combustible = input("Tipo de combustible: ") 
    
    carro = Carro_Deportivo(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)
    bd.agregar_vehiculo(carro)
    print("Carro deportivo creado y registrado.")
    
    # Demostración de funcionalidades
    carro.arranque()
    carro.aceleracion()
    carro.sistema_direccion()
    carro.tipo_seguridad()

def crear_chana_furgon():
    modelo = input("Modelo (ej: Chana Furgón 2023): ") 
    color = input("Color (ej: Blanco): ") 
    motor = input("Motor (ej: 1.5L): ") 
    numero_puertas = input("Número de puertas: ") 
    capacidad_pasajeros = input("Capacidad de pasajeros: ") 
    tipo_combustible = input("Tipo de combustible: ") 
    
    furgon = Chana_Furgon(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)
    bd.agregar_vehiculo(furgon)
    print("Chana furgón creado y registrado.")
    
    furgon.arranque()
    furgon.frenado()
    furgon.sistema_ventanas()
    furgon.luces()

def crear_volqueta():
    modelo = input("Modelo (ej: Volvo FMX): ") 
    color = input("Color (ej: Amarillo): ") 
    motor = input("Motor (ej: Diésel 13L): ") 
    numero_puertas = input("Número de puertas: ") 
    capacidad_pasajeros = input("Capacidad de pasajeros: ") 
    tipo_combustible = input("Tipo de combustible: ") 
    
    volqueta = Volqueta(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)
    bd.agregar_vehiculo(volqueta)
    print("Volqueta creada y registrada.")
    
    volqueta.arranque()
    volqueta.aceleracion()
    volqueta.sistema_espejos()
    volqueta.tipo_seguridad()

def crear_vehiculo_normal():
    modelo = input("Modelo: ") 
    color = input("Color: ") 
    motor = input("Motor: ") 
    numero_puertas = input("Número de puertas: ") 
    capacidad_pasajeros = input("Capacidad de pasajeros: ") 
    tipo_combustible = input("Tipo de combustible: ") 
    
    vehiculo = Vehiculo(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)
    bd.agregar_vehiculo(vehiculo)
    print("Vehículo normal creado y registrado.")
    
    vehiculo.arranque()
    vehiculo.climatizacion()
    vehiculo.luces()
    vehiculo.sistema_ventanas()

def ver_listas():
    while True:
        opcion = menu_ver_listas()
        if opcion == "1":
            print("\n--- Todos los vehículos ---")
            bd.imprimir_info()
        elif opcion == "2":
            print("\n--- Carros deportivos ---")
            bd.imprimir_info(filtro_tipo="Carro_Deportivo")
        elif opcion == "3":
            print("\n--- Chana furgones ---")
            bd.imprimir_info(filtro_tipo="Chana_Furgon")
        elif opcion == "4":
            print("\n--- Volquetas ---")
            bd.imprimir_info(filtro_tipo="Volqueta")
        elif opcion == "5":
            print("\n--- Vehículos normales ---")
            lista = [v for v in bd.lista_vehiculos if v.__class__.__name__ == "Vehiculo"]
            if not lista:
                print("No hay vehículos de ese tipo.")
            else:
                for i, vehiculo in enumerate(lista):
                    print(f"{i}. ", end="")
                    vehiculo.mostrar_atributos()
        elif opcion == "6":
            break
        else:
            print("Opción no válida en Ver listas.")

def eliminar_vehiculo():
    if not bd.lista_vehiculos:
        print("No hay vehículos para eliminar.")
        return
    print("\n--- Eliminar vehículo ---")
    for i, vehiculo in enumerate(bd.lista_vehiculos):
        print(f"{i}. ", end="")
        vehiculo.mostrar_atributos()
    try:
        indice = int(input("Ingresa el número del vehículo que deseas eliminar: "))
        if 0 <= indice < len(bd.lista_vehiculos):
            eliminada = bd.eliminar_por_indice(indice)
            print(f"Vehículo eliminado")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor ingresa un número válido.")

def main():
    while True:
        opcion = menu_principal()
        if opcion == "1":
            crear_carro_deportivo()
        elif opcion == "2":
            crear_chana_furgon()
        elif opcion == "3":
            crear_volqueta()
        elif opcion == "4":
            crear_vehiculo_normal()
        elif opcion == "5":
            ver_listas()
        elif opcion == "6":
            eliminar_vehiculo()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()