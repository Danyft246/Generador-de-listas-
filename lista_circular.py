class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.primero = None

    def esta_vacia(self):
        return self.primero is None

    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            nuevo.siguiente = nuevo
            self.primero = nuevo
            return
        aux = self.primero
        while aux.siguiente != self.primero:
            aux = aux.siguiente
        aux.siguiente = nuevo
        nuevo.siguiente = self.primero

    def mostrar(self):
        if self.esta_vacia():
            return "Lista circular vacía"
        elementos = []
        aux = self.primero
        while True:
            elementos.append(str(aux.dato))
            aux = aux.siguiente
            if aux == self.primero:
                break
        return " -> ".join(elementos) + f" -> (vuelve a {self.primero.dato})"