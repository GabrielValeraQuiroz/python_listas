import time
import threading
import keyboard
import random

num = 6
bandera = False

class Intervalo:
    def __init__(self, func, tiempo):
        self.func = func
        self.tiempo = tiempo
        self.timer = None
        self.running = False
        
    def iniciar(self):
        self.running = True
        self.ejecutar()
        
    def ejecutar(self):
        if self.running:
            self.func()
            self.timer = threading.Timer(self.tiempo, self.ejecutar)
            self.timer.start()
        
    def cancelar(self):
        self.running = False
        if self.timer:
            self.timer.cancel()

def mostrar_menu():
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas pendientes")
    print("4. Ruleta de tareas")
    print("5. Salir")

def agregar_tarea(tareas, tarea):
    tareas.append(tarea)
    print("Tarea agregada exitosamente!")

def eliminar_tarea(tareas, indice):
    if 0 <= indice < len(tareas):
        tarea_eliminada = tareas.pop(indice)
        print("Tarea eliminada:", tarea_eliminada)
    else:
        print("Índice de tarea inválido")

def mostrar_tareas(tareas):
    if tareas:
        print("Tareas pendientes:")
        for i, tarea in enumerate(tareas):
            print(f"{i + 1}. {tarea}")
    else:
        print("No hay tareas pendientes")

def siuu():
    global num
    num-=1
    print(num)
tareas = []
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        tarea = input("Ingrese la nueva tarea: ")
        agregar_tarea(tareas, tarea)
    elif opcion == "2":
        indice = int(input("Ingrese el índice de la tarea a eliminar: ")) - 1
        eliminar_tarea(tareas, indice)
    elif opcion == "3":
        mostrar_tareas(tareas)
    elif opcion == "4":
        if bandera:
            while True:
                print("Volviste!!! Cuentame, terminaste? Presiona Y/N")
                opcion = keyboard.read_hotkey()
                if opcion == "Y":
                    print("TU RECOMPENSA ES HABER LOGRADO TUS OBJETIVOS")
                    break
                elif opcion == "N":
                    print("Fuera, que haces aqui?")
                    break
                else:
                    print("Opción invalida")
        else :
            tarea = print("No sabes por donde empezar? Gira la ruleta, completa la tarea y obten un premio :D")
            print("Toca el espacio para girar")
            keyboard.wait('space')
            intervalo = Intervalo(siuu, 1)
            intervalo.iniciar()
            time.sleep(5)
            intervalo.cancelar()
            sum = 6
            if len(tareas) > 0 :
                print("Te toco: " + tareas[random.randrange(0,len(tareas))])
                print("Vuelve cuando hayas terminado!!!")
            else :
                print("VAYA, haz acabado todas tus tareas. Je.")
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione nuevamente.")