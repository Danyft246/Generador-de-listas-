class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaSimple:
    def __init__(self):
        self.primero = None

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.primero
        self.primero = nuevo

    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if self.primero is None:
            self.primero = nuevo
            return
        aux = self.primero
        while aux.siguiente is not None:
            aux = aux.siguiente
        aux.siguiente = nuevo

    def buscar(self, dato):
        aux = self.primero
        while aux is not None:
            if aux.dato == dato:
                return aux
            aux = aux.siguiente
        return None

    def eliminar_primero(self):
        if self.primero is not None:
            self.primero = self.primero.siguiente
            return True
        return False

    def eliminar_nodo(self, dato):
        if self.primero is None:
            return False
        if self.primero.dato == dato:
            self.primero = self.primero.siguiente
            return True
        aux = self.primero
        while aux.siguiente is not None and aux.siguiente.dato != dato:
            aux = aux.siguiente
        if aux.siguiente is not None:
            aux.siguiente = aux.siguiente.siguiente
            return True
        return False

    def mostrar(self):
        if not self.primero:
            return "Lista vacía"
        aux = self.primero
        elementos = []
        while aux:
            elementos.append(str(aux.dato))
            aux = aux.siguiente
        return " -> ".join(elementos) + " -> None"