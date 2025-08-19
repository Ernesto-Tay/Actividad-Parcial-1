estudiantes = {}
class Estudiante:
    def __init__(self,Carnet,Nombre,Carrera):
        self.Carnet = Carnet
        self.Nombre = Nombre
        self.Carrera = Carrera
        self.Actividades = {}

class Actividad:
    def __init__(self,Nombre,Fecha,Categoria,prioridad):
        self.Nombre = Nombre
        self.Fecha = Fecha
        self.Categoria = Categoria
        self.prioridad = prioridad
