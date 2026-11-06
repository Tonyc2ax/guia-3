from pasajero import Pasajero


class MiCola:
    """Cola (FIFO) hecha a mano sobre un arreglo de tamaño fijo."""

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def encolar(self, pasajero):
        if self.cantidad == self.capacidad:
            print("La cola está llena")
            return False

        self.datos[self.cantidad] = pasajero
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):
        if self.cantidad == 0:
            print("(cola vacía)")
            return

        for i in range(self.cantidad):
            if i == 0:
                print(f"[{i}] {self.datos[i]} <- FRENTE")
            elif i == self.cantidad - 1:
                print(f"[{i}] {self.datos[i]} <- FINAL")
            else:
                print(f"[{i}] {self.datos[i]}")

    def desencolar(self):
        if self.cantidad == 0:
            return None

        Pasajero = self.datos[0]

        for i in range(self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]

        self.cantidad = self.cantidad - 1
        self.datos[self.cantidad] = None

        return Pasajero

    def ver_frente(self):
        if self.cantidad == 0:
            return None

        Pasajero = self.datos[0]
        return Pasajero

    def buscar(self, numero):
        if self.cantidad == 0:
            return None

        for i in range(self.cantidad):
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

        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                for j in range(i, self.cantidad - 1):
                    self.datos[j] = self.datos[j + 1]

                self.cantidad = self.cantidad - 1
                self.datos[self.cantidad] = None

                return True

        return False

    def copiar(self):
        nueva = MiCola(self.capacidad)

        for i in range(self.cantidad):
            nueva.encolar(self.datos[i])

        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        if self.cantidad == 0:
            return True
        else:
            return False

    def ordenar_asc(self):
        for i in range(self.cantidad - 1):
            for j in range(self.cantidad - 1 - i):
                if self.datos[j].numero > self.datos[j + 1].numero:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux

    def ordenar_desc(self):
        for i in range(self.cantidad - 1):
            for j in range(self.cantidad - 1 - i):
                if self.datos[j].numero < self.datos[j + 1].numero:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux

    def buscar_binaria(self, cedula):
        inicio = 0
        fin = self.cantidad - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2

            if self.datos[medio].numero == cedula:
                return self.datos[medio]

            if self.datos[medio].numero < cedula:
                inicio = medio + 1
            else:
                fin = medio - 1

        return None

    def reversar(self):
        ult = self.cantidad - 1
        pri = 0

        while pri < ult:
            aux = self.datos[pri]
            self.datos[pri] = self.datos[ult]
            self.datos[ult] = aux

            pri = pri + 1
            ult = ult - 1

    def filtrar_mayores_de_edad(self):
        nueva = MiCola(self.capacidad)

        for i in range(self.cantidad):
            Pasajero = self.datos[i]

            if Pasajero.edad >= 18:
                nueva.encolar(Pasajero)

        return nueva

    def nombres_en_mayusculas(self):
        for i in range(self.cantidad):
            Pasajero = self.datos[i]
            Pasajero.nombre = Pasajero.nombre.upper()
