from threading import Thread, Condition
from random import randint
import time

#Max recaudado: 2000€
dineroCuenta = 0

class Voluntario(Thread):

    cond = Condition() #Se usara para notificar los voluntarios cuando pueden recaudar el dinero.

    def __init__(self, name):
        Thread.__init__(self, name=name)
    
    def run(self):
        dinero = randint(4, 25) #Range: 4€ y 25€
        print(f"{self.name} ha salido a la calle y empieza a recaudar el dinero.")
        with Voluntario.cond:
            pass

class Gestor(Thread):

    cond = Condition() #Se usara para notificar los gestores cuando pueden gestionar el dinero recaudado.

    def __init__(self, name):
        Thread.__init__(self, name=name)

    def run(self):
        global dineroCuenta
        dinero = randint(10, 41) #Range: 10€ y 40€
        print(f"{self.name} esta listo para gestionar el dinero recaudado.")
        with Gestor.cond:
            pass

if __name__ == "__main__":
    listaGestores = [] #len=4
    listaVoluntarios = [] #len=4
    for i in range(0,4): #Se crean hilos demonio que nunca pararan de ejecutarse hasta que se termine el hilo principal (main).
        currentThread = Gestor(f"Gestor {i}")
        currentThread1 = Voluntario(f"Voluntario {i}")
        currentThread.daemon = True
        currentThread1.daemon = True
        listaGestores.append(currentThread)
        listaVoluntarios.append(currentThread1)
    for voluntario in listaVoluntarios: #Se inician todos los hilos.
        voluntario.start()
    for gestor in listaGestores:
        gestor.start()