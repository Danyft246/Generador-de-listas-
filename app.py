from flask import Flask, render_template, request, jsonify
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from lista_simple import ListaSimple
from lista_doble import ListaDoble
from lista_circular import ListaCircular

app = Flask(__name__)

listas = {
    "simple": ListaSimple(),
    "doble": ListaDoble(),
    "circular": ListaCircular()
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/<tipo>/insertar', methods=['POST'])
def insertar(tipo):
    data = request.json
    dato = data.get('dato')
    posicion = data.get('posicion', 'final')
    
    if tipo not in listas: return jsonify({"error": "Tipo inválido"}), 400
    lista = listas[tipo]
    try:
        if tipo in ["simple", "doble"]:
            if posicion == "inicio":
                lista.insertar_inicio(dato)
            else:
                lista.insertar_final(dato)
        else:
            lista.insertar_final(dato)
        return jsonify({"status": "ok", "lista": obtener_estado(lista, tipo)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/<tipo>/eliminar', methods=['POST'])
def eliminar(tipo):
    data = request.json
    dato = data.get('dato')
    accion = data.get('accion', 'primero')
    
    if tipo not in listas: return jsonify({"error": "Tipo inválido"}), 400
    lista = listas[tipo]
    success = False
    try:
        if tipo in ["simple", "doble"]:
            if accion == 'primero' or dato is None:
                success = lista.eliminar_primero()
            elif accion == 'ultimo':
                if lista.primero is None:
                    success = False
                elif getattr(lista.primero, 'siguiente', None) is None:
                    lista.primero = None
                    success = True
                else:
                    aux = lista.primero
                    while aux.siguiente and aux.siguiente.siguiente:
                        aux = aux.siguiente
                    aux.siguiente = None
                    success = True
            else:
                success = lista.eliminar_nodo(dato)
        # Circular: eliminación básica
        elif tipo == "circular" and dato:
            success = lista.eliminar_nodo(dato) if hasattr(lista, 'eliminar_nodo') else False
        return jsonify({"status": "ok", "success": success, "lista": obtener_estado(lista, tipo)})
    except:
        return jsonify({"status": "ok", "success": False, "lista": obtener_estado(lista, tipo)})

@app.route('/api/<tipo>/buscar', methods=['POST'])
def buscar(tipo):
    data = request.json
    dato = data.get('dato')
    if tipo not in listas: return jsonify({"error": "Tipo inválido"}), 400
    lista = listas[tipo]
    encontrado = False
    try:
        if tipo == "simple":
            encontrado = lista.buscar(dato) is not None
        elif tipo == "doble":
            aux = lista.primero
            while aux:
                if str(aux.dato) == str(dato):
                    encontrado = True
                    break
                aux = aux.siguiente
    except:
        pass
    return jsonify({"status": "ok", "encontrado": encontrado})

@app.route('/api/<tipo>/mostrar_inverso', methods=['GET'])
def mostrar_inverso(tipo):
    if tipo != "doble": return jsonify({"error": "Solo para doble"}), 400
    lista = listas[tipo]
    return jsonify({"lista": lista.mostrar_inverso() if hasattr(lista, 'mostrar_inverso') else "No disponible"})

@app.route('/api/<tipo>/estado', methods=['GET'])
def estado(tipo):
    if tipo not in listas: return jsonify({"error": "Tipo inválido"}), 400
    return jsonify({"lista": obtener_estado(listas[tipo], tipo)})

def obtener_estado(lista, tipo):
    return lista.mostrar() if hasattr(lista, 'mostrar') else "Estado no disponible"

@app.route('/api/reset', methods=['POST'])
def reset():
    global listas
    listas = {"simple": ListaSimple(), "doble": ListaDoble(), "circular": ListaCircular()}
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    os.makedirs('templates', exist_ok=True)
    app.run(debug=True, port=5000)