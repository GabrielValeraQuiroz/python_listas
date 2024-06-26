def mostrar_menu():
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas pendientes")
    print("4. Salir")

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

def main():
    tareas = []
    tareasd = []
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
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")

if __name__ == "__main__":
    main()