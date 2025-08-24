class Actividades:
    def __init__(self):
        self.actividades  = {}

    def buscar_por_palabra(self):
        palabra=input("Ingrese palabra para buscar actividad:")
        resultado= []
        for actividad in self.actividades.values():
            if palabra in actividad.nombre.lower() or palabra in actividad.curso.lower():
                resultado.append(actividad)
        if resultado:
            print(f"Resultados de la palabra {palabra}")
            for acti in resultado:
                print(acti)
        else:
            print("No pudimos encontrar resultados :(...")


class Actividad:
    def __init__(self,ID,nombre,fecha,hora,prioridad,curso):
        self.ID = ID
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora
        self.categoria = ""
        self.prioridad = prioridad
        self.curso = curso

class Clase(Actividad):
    def __init__(self,ID,nombre,fecha,hora,prioridad,curso):
        super().__init__(ID,nombre,fecha,hora,prioridad,curso)
        self.categoria = "Clase"

class Examen(Actividad):
    def __init__(self,ID,nombre,fecha,hora,prioridad,curso):
        super().__init__(ID,nombre,fecha,hora,prioridad,curso)
        self.categoria = "Examen"

class Tarea(Actividad):
    def __init__(self,ID,nombre,fecha,hora,prioridad,curso):
        super().__init__(ID,nombre,fecha,hora,prioridad,curso)
        self.categoria = "Tarea"

class Reunion(Actividad):
    def __init__(self,ID,nombre,fecha,hora,prioridad,curso):
        super().__init__(ID,nombre,fecha,hora,prioridad,curso)
        self.categoria = "Reunion"

class Evento(Actividad):
    def __init__(self,ID,nombre,fecha,hora,prioridad,curso):
        super().__init__(ID,nombre,fecha,hora,prioridad,curso)
        self.categoria = "Evento"

        
def menu():
    print("---MENÚ---")
    print(f"1.Agrgear Actividad\n2.Listar actividades.\n3.Buscar por palabras.\n4.Eliminar actividades.")
    print("5.Salir.")
while True:
    menu()
    opcion= input("Ingrese una opcion:")
    match opcion:
        case "1":
            print("---AGREGAR ACTIVIDAD---")
        case "2":
            print("---LISTAR ACTIVIDADES---")
        case "3":
            print("---BUSCAR POR PALABRAS---")
        case "4":
            print("---ELIMINAR ACTIVIDAD---")
        case "5":
            print("Saliendo del programa...")
            break
        case _:
            print("Opcion no valida...")
