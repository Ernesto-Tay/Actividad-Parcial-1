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
                if (actividad.fecha_completa.isocalender()[1] == hoy.isocalendar()[1] and
                    actividad.fecha_completa.vear == hoy.ver):
                    resultados.append(actividad)
        elif tipo_filtro == "categoria":
            #filtro por una categoria especifica que el usuario haya querido ingresar (puedeo ser cualquiera: tareas, examenes, etc)
            for actividad in self.actividades.values():
                if actividad.categoria.lower() == valor.lower():
                    resultados.append(actividad)
        else:
            print(f"---TIPO DE FILTRO NO VALIDO (INTENTE DE NUEVO)---")
            return

        ''' aqui estamos mostrando los resultados si se encuentran 
        dentro de nuestro diccionario de'''
        if resultados:
            print(f"\n---ACTIVIDADES FILTRADAS POR '{tipo_filtro}' ---")
            for actividad in resultados:
                print(actividad)
        else:
            print(f"\n----------NO SE ENCONTRO NINGUNA ACTIVIDAD CON ESE FILTRO (NOMBRE)---------")



class Actividad:
    def __init__(self,ID,nombre,fecha,hora,prioridad,curso):
        self.ID = ID
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora
        self.categoria = ""
        self.prioridad = prioridad
        self.curso = curso
        #modificacion de la primera clase
        self.fecha_completa = datetime.strptime(f"{fecha} {hora}", '%Y-%m-%d %H:%M')

    def __str__(self):
        "Devuelve una representacion de la actividad en formato de cadena"
        return(
            f"ID: {self.ID}, Nombre: {self.nombre}, Categoria: {self.categoria},"
            f"Fecha: {self.fecha_completa.strftime('%Y-%m-%d %H:%M')},"
            f"Prioridad:{self.prioridad}, Curso: {self.curso}"

        )
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

# Función principal para la interacción del usuario.
def main():
    gestor_actividades = Actividades()

    while True:
        print("\n-------MENU DE GESTION DE ACTIVIDADES PERSONALES ------")
        print(f"1. ---AGREGAR NUEVA ACTIVIDAD CON FECHA, CATEGORIA Y PRIORIDAD---")
        print(f"2. ---Listar actividades POR: DIA, SEMANA O CATEGORIA---")
        print(f"3. ---BUSCAR POR PALABRAS CLAVE---")
        print(f"4. ---ELIMINAR ACTIVIDADES PASADAS---")
        print(f"5. ---Salir---")
        opcion = input("Elige una opción(1-3): ")

        # usamos match case para hacer nuestro codigo más ordnado para evitar usar
        # condicionales if-else
        match opcion:
            case '1':
                # Solicita los datos para agregar la nueva actividad
                ID = input(" INGRESE ID PARA LA ACTIVIDAD: ")
                if ID in gestor_actividades.actividades:
                    print("--- El ID ya existe. Por favor, intente un ID diferente---")
                    continue
                nombre = input("-----INGRESE NOMBRE DE LA ACTIVIDAD: ")
                fecha = input("-----INGRESE FECHA DE LA ACTIVIDAD (YYYY-MM-DD): ")
                hora = input("-----INGRESE HORA DE LA ACTIVIDAD (HH:MM): ")
                prioridad = input("----- INGRESE LA PRIORIDAD (Alta/Media/Baja): ")
                curso = input("----- INGRESE EL CURSO AL QUE PERTENECE LA ACTIVIDAD: ")

                categoria_opcion = input("Categoría (Clase, Examen, Tarea, Reunion, Evento): ").lower()
                nueva_actividad = None
                # una variable a la cual se le asigna 'none' es porque es una varible
                # la cual esta esperando recibir algun valor, para que esta no cause conflicto o algun
                # error en el codigo, se inicializa de esta manera


                # utilizamos estructura 'match case' para crear la subclase correcta
                # anteriormente ya creamos todas las subclases de las distintas actividades que
                # el usuario puede crear cuando escoge alguna en especifico
                # cuando el usuario eliga una, los parametros que solicitamos, seran
                # agregados a la padre y luego esta ira heredando a quien corresponda clase correcta sin afectar las demas
                match categoria_opcion:
                    case 'clase':
                        nueva_actividad = Clase(ID, nombre, fecha, hora, prioridad, curso)
                    case 'examen':
                        nueva_actividad = Examen(ID, nombre, fecha, hora, prioridad, curso)
                    case 'tarea':
                        nueva_actividad = Tarea(ID, nombre, fecha, hora, prioridad, curso)
                    case 'reunion':
                        nueva_actividad = Reunion(ID, nombre, fecha, hora, prioridad, curso)
                    case 'evento':
                        nueva_actividad = Evento(ID, nombre, fecha, hora, prioridad, curso)
                    case _:
                        print("----------CATEGORIA NO VALIDA----------")





