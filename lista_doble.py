class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class ListaDoble:
    def __init__(self):
        self.primero = None

    def esta_vacia(self):
        return self.primero is None

    def insertar_inicio(self, dato):
        nuevo = NodoDoble(dato)
        if self.esta_vacia():
            self.primero = nuevo
            return
        nuevo.siguiente = self.primero
        self.primero.anterior = nuevo
        self.primero = nuevo

    def insertar_final(self, dato):
        nuevo = NodoDoble(dato)
        if self.esta_vacia():
            self.primero = nuevo
            return
        aux = self.primero
        while aux.siguiente is not None:
            aux = aux.siguiente
        aux.siguiente = nuevo
        nuevo.anterior = aux

    def eliminar_primero(self):
        if self.esta_vacia():
            return False
        if self.primero.siguiente is None:
            self.primero = None
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None
        return True

    def eliminar_nodo(self, dato):
        if self.esta_vacia():
            return False
        aux = self.primero
        while aux and aux.dato != dato:
            aux = aux.siguiente
        if not aux:
            return False
        if aux.anterior is None:
            self.primero = aux.siguiente
            if self.primero:
                self.primero.anterior = None
        elif aux.siguiente is None:
            aux.anterior.siguiente = None
        else:
            aux.anterior.siguiente = aux.siguiente
            aux.siguiente.anterior = aux.anterior
        return True

    def mostrar(self):
        if self.esta_vacia():
            return "Lista doble vacía"
        aux = self.primero
        elementos = []
        while aux:
            elementos.append(str(aux.dato))
            aux = aux.siguiente
        return " <-> ".join(elementos) + " <-> None"

    def mostrar_inverso(self):
        if self.esta_vacia():
            return "Lista doble vacía"
        aux = self.primero
        while aux.siguiente:
            aux = aux.siguiente
        elementos = []
        while aux:
            elementos.append(str(aux.dato))
            aux = aux.anterior
        return " <-> ".join(elementos) + " <-> None"