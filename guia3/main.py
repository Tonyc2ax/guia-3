
from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola

pila = MiPila(10)
cola = MiCola(10)



def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ser un numero entero.")


def leer_pasajero():
    numero = leer_entero("Numero de pasajero: ")
    nombre = input("Nombre: ").strip()
    cedula = input("Cedula: ").strip()
    edad = leer_entero("Edad: ")
    fecha = input("Fecha de vuelo: ").strip()
    destino = input("Destino: ").strip()
    asiento = input("Asiento: ").strip().upper()

    return Pasajero(numero, nombre, cedula, edad,
                    fecha, destino, asiento)


def datos_prueba():
    return [
        Pasajero(1005, "Diana", "0923456789", 22,
                 "2026-11-15", "Quito", "12A"),
        Pasajero(1002, "Ana", "0912345678", 28,
                 "2026-11-15", "Lima", "03C"),
        Pasajero(1009, "Luis", "0987654321", 35,
                 "2026-11-20", "Bogota", "18F"),
        Pasajero(1004, "Beto", "0934567890", 16,
                 "2026-11-20", "Quito", "07B"),
        Pasajero(1001, "Elena", "0901234567", 41,
                 "2026-11-22", "Lima", "01A")
    ]


def mostrar_opciones(titulo, entrar, salir, ver):
    print("\n==========", titulo, "==========")
    print("1.", entrar, "  2. Listar  3.", salir)
    print("4.", ver, "  5. Buscar  6. Modificar")
    print("7. Eliminar por numero  8. Copiar")
    print("9. Longitud / ¿Vacia?")
    print("C. Cargar datos de prueba  0. Volver")


# MENU DE PILA

def menu_pila():
    while True:
        mostrar_opciones("MENU PILA (LIFO)", "Apilar",
                         "Desapilar", "Ver tope")

        op = input("Opcion: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()

            if pila.apilar(pasajero):
                print("Pasajero apilado correctamente.")

        elif op == "2":
            pila.listar()

        elif op == "3":
            pasajero = pila.desapilar()

            if pasajero is None:
                print("La pila esta vacia.")
            else:
                print("Pasajero desapilado:")
                print(pasajero)

        elif op == "4":
            pasajero = pila.ver_tope()

            if pasajero is None:
                print("La pila esta vacia.")
            else:
                print("Tope de la pila:")
                print(pasajero)

        elif op == "5":
            numero = leer_entero("Numero que desea buscar: ")
            posicion = pila.buscar(numero)

            if posicion == -1:
                print("Pasajero no encontrado.")
            else:
                print("Encontrado en la posicion:", posicion)
                print(pila.datos[posicion])

        elif op == "6":
            numero = leer_entero("Numero del pasajero: ")
            destino = input("Nuevo destino: ").strip()
            asiento = input("Nuevo asiento: ").strip().upper()

            if pila.modificar(numero, destino, asiento):
                print("Pasajero modificado.")
            else:
                print("Pasajero no encontrado.")

        elif op == "7":
            numero = leer_entero("Numero que desea eliminar: ")

            if pila.eliminar_por_numero(numero):
                print("Pasajero eliminado.")
            else:
                print("Pasajero no encontrado.")

        elif op == "8":
            nueva = pila.copiar()
            print("Copia de la pila:")
            nueva.listar()

        elif op == "9":
            print("Longitud:", pila.longitud())

            if pila.esta_vacia():
                print("La pila esta vacia.")
            else:
                print("La pila tiene pasajeros.")

        elif op == "C":
            for p in datos_prueba():
                pila.apilar(p)

            print("Datos de prueba cargados.")

        elif op == "0":
            break

        else:
            print("Opcion no valida.")


# MENU DE COLA

def menu_cola():
    while True:
        mostrar_opciones("MENU COLA (FIFO)", "Encolar",
                         "Desencolar", "Ver frente")

        op = input("Opcion: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()

            if cola.encolar(pasajero):
                print("Pasajero encolado correctamente.")

        elif op == "2":
            cola.listar()

        elif op == "3":
            pasajero = cola.desencolar()

            if pasajero is None:
                print("La cola esta vacia.")
            else:
                print("Pasajero desencolado:")
                print(pasajero)

        elif op == "4":
            pasajero = cola.ver_frente()

            if pasajero is None:
                print("La cola esta vacia.")
            else:
                print("Frente de la cola:")
                print(pasajero)

        elif op == "5":
            numero = leer_entero("Numero que desea buscar: ")
            posicion = cola.buscar(numero)

            if posicion == -1:
                print("Pasajero no encontrado.")
            else:
                print("Encontrado en la posicion:", posicion)
                print(cola.datos[posicion])

        elif op == "6":
            numero = leer_entero("Numero del pasajero: ")
            destino = input("Nuevo destino: ").strip()
            asiento = input("Nuevo asiento: ").strip().upper()

            if cola.modificar(numero, destino, asiento):
                print("Pasajero modificado.")
            else:
                print("Pasajero no encontrado.")

        elif op == "7":
            numero = leer_entero("Numero que desea eliminar: ")

            if cola.eliminar_por_numero(numero):
                print("Pasajero eliminado.")
            else:
                print("Pasajero no encontrado.")

        elif op == "8":
            nueva = cola.copiar()
            print("Copia de la cola:")
            nueva.listar()

        elif op == "9":
            print("Longitud:", cola.longitud())

            if cola.esta_vacia():
                print("La cola esta vacia.")
            else:
                print("La cola tiene pasajeros.")

        elif op == "C":
            for p in datos_prueba():
                cola.encolar(p)

            print("Datos de prueba cargados.")

        elif op == "0":
            break

        else:
            print("Opcion no valida.")


def main():
    while True:
        print("\n===== TAREA PILAS Y COLAS =====")
        print("1. Menu de pila")
        print("2. Menu de cola")
        print("3. Salir")

        op = input("Opcion: ").strip()

        if op == "1":
            menu_pila()

        elif op == "2":
            menu_cola()

        elif op == "3":
            print("Hasta pronto.")
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
