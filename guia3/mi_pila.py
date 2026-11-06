from pasajero import Pasajero


class MiPila:
    """Pila (LIFO) hecha a mano sobre un arreglo de tamaño fijo."""

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def apilar(self, pasajero):
        if self.cantidad == self.capacidad:
            print("La pila está llena")
            return False

        self.datos[self.cantidad] = pasajero
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):
        if self.cantidad == 0:
            print("(pila vacía)")
            return

        for i in range(self.cantidad - 1, -1, -1):
            if i == self.cantidad - 1:
                print(f"[{i}] {self.datos[i]} <- TOPE")
            elif i == 0:
                print(f"[{i}] {self.datos[i]} <- FONDO")
            else:
                print(f"[{i}] {self.datos[i]}")

    def desapilar(self):
        if self.cantidad == 0:
            return None

        Pasajero = self.datos[self.cantidad - 1]
        self.cantidad = self.cantidad - 1
        self.datos[self.cantidad] = None

        return Pasajero

    def ver_tope(self):
        if self.cantidad == 0:
            return None

        Pasajero = self.datos[self.cantidad - 1]
        return Pasajero

    def buscar(self, numero):
        if self.cantidad == 0:
            return None

        for i in range(self.cantidad - 1, -1, -1):
            if self.datos[i].numero == numero:
                return self.datos[i]

        return None

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pasajero = self.buscar(numero)

        if pasajero is None:
            return False

        pasajero.destino = nuevo_destino
        pasajero.asiento = nuevo_asiento

        return True

    def eliminar_por_numero(self, numero):
        pasajero = self.buscar(numero)

        if pasajero is None:
            return False

        for i in range(self.cantidad - 1, -1, -1):
            if self.datos[i].numero == numero:

                for j in range(i, self.cantidad - 1):
                    self.datos[j] = self.datos[j + 1]

                self.cantidad = self.cantidad - 1
                self.datos[self.cantidad] = None

                return True

        return False

    def copiar(self):
        nueva = MiPila(self.capacidad)

        for i in range(self.cantidad):
            nueva.apilar(self.datos[i])

        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        if self.cantidad == 0:
            return True
        else:
            return False
