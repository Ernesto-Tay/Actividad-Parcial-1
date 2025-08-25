from datetime import datetime
class Actividades:
    def __init__(self):
        self.actividades  = {}

    def eliminar_actividades_pasada(self):
        fecha_actual= datetime.now()
        actividades_pasadas= []

        for actividad in self.actividades.values():
            if actividad.fecha < fecha_actual:
                actividades_pasadas.append(actividad)
        if not actividades_pasadas:
            print("No tienes actividades pasadas para eliminar:")

        print("---ACTIVIDADES PASADAS---")
        for actividades in actividades_pasadas:
            print(actividades)

        opcion= input("Dese eliminar todas las actividades pasadas? (si/no:)").lower()
        match opcion:
            case "si":
                for activi in actividades_pasadas:
                    def self.actividades[activi.ID]
                print(f"Se eliminaron {len(actividades_pasadas)} actividades pasadas")
            case _:
                print("No se elimino ninguna actividad.")
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

