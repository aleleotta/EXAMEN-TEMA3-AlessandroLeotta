from Cliente import *

if __name__ == "__main__":
    listaClientes = [] #len=10
    for i in range(0,10): #Por cada ciclo se crea un nuevo cliente y se almacena en la lista, el hilo todavia no se ejecuta.
        currentThread = Cliente(f"Cliente {i}")
        listaClientes.append(currentThread)
    for cliente in listaClientes: #Se ejecutan todos los hilos.
        cliente.start()