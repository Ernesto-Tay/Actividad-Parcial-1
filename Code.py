#clase para crear una actividad
#o varias actividades

#exportacion de las librerias para la manipulacion del tiempo

from datetime import datetime
class Actividades:
    def __init__(self):
        self.actividades  = {}

    def agregar_activiad(self,actividad):
        #agregaremos una nueva actividad al diccionario
        self.actividades[actividad.ID] = actividad
        print(f"---ACTIVIDAD {actividad.ID} con ID: {actividad.ID}---")

    def listar_por_filtro(self,tipo_filtro, valor=""):
        resultados = []
        hoy = datetime.now()

        #condicionales para determinar el tipo de filtro a aplicar para cada activiad agregada
        if tipo_filtro == "dia":
            # aqui filtramos por el dia actual
            for actividad in self.actividades.values():
                if actividad.fecha_completa.date() == hoy.date():
                    resultados.append(actividad)
        elif tipo_filtro == "semana":
            # aqui filtramos por semana actual
            for actividad in self.actividades.value():
                #aqui comparamos el numero de semana ISO y el año para la coincidencia
                if (actividad.fecha_completa)




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



