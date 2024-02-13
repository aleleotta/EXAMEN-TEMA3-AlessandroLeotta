from threading import Thread, Semaphore
from random import randint
import time

class Cliente(Thread):

    semaphore = Semaphore(2) #Se usa un Semaphore(2) para tener 2 filas para dos maquinas
    semaphore1 = Semaphore(5) #Se usa un Semaphore(5) para tener 5 filas para 5 dependientes

    def __init__(self, name): #Constructor de hilos.
        Thread.__init__(self, name=name)

    def run(self):
        print(f"{self.name} esta en la fila para recojer el ticket.\n")
        
        Cliente.semaphore.acquire() #Seccion critica para cuando el cliente recoje el ticket.
        print(f"{self.name} es primero en la fila y esta recogiendo el ticket.\n")
        time.sleep(randint(0,4)) #Se espera de 1 a 4 segundos.
        Cliente.semaphore.release()

        print(f"{self.name} esta en la fila para recojer la comida.\n")
        
        Cliente.semaphore1.acquire() #Seccion critica para cuando el cliente recoje la comida.
        time.sleep(randint(3, 8)) #Se espera de 3 a 7 segundos.
        print(f"{self.name} es el primero en la fila para recojer la comida.\n")
        Cliente.semaphore1.release()
        
        print(f"{self.name} se pone a comer.\n")
        time.sleep(randint(2, 5)) #Tiempo para comer y marcharse.
        print(f"{self.name} se marcha.\n")