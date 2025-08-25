# clase para crear una actividad
# o varias actividades
# exportacion de las librerias para la manipulacion del tiempo

from datetime import datetime
class Actividades:
    def __init__(self):
        self.actividades  = {}


    def agregar_actividad(self,actividad):
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
            for actividad in self.actividades.values():
                #aqui comparamos el numero de semana ISO y el año para la coincidencia
                if (actividad.fecha_completa.isocalender()[1] == hoy.isocalendar()[1] and
                    actividad.fecha_completa.vear == hoy.year):
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
        
    
    def buscar_por_palabra(self):
        palabra = input("Ingrese palabra para buscar actividad: ").lower()
        resultado = []
        for actividad in self.actividades.values():
            if palabra in actividad.nombre.lower() or palabra in actividad.curso.lower():
                resultado.append(actividad)
        if resultado:
            print(f"Resultados de la palabra '{palabra}':")
            for acti in resultado:
                print(f"{acti.ID} - {acti.nombre} ({acti.categoria})")
        else:
            print("No pudimos encontrar resultados :(")

    
    def eliminar_actividades_pasada(self):
        fecha_actual = datetime.now()
        actividades_pasadas = []

        for actividad in self.actividades.values():
            # Convertir fecha de la actividad a datetime
            try:
                fecha_actividad = datetime.strptime(actividad.fecha, "%Y-%m-%d")
            except ValueError:
                print(f"Formato de fecha inválido en la actividad {actividad.ID}")
                continue

            if fecha_actividad < fecha_actual:
                actividades_pasadas.append(actividad)

        if not actividades_pasadas:
            print("No tienes actividades pasadas para eliminar.")
            return

        print("---ACTIVIDADES PASADAS---")
        for act in actividades_pasadas:
            print(f"{act.ID} - {act.nombre} ({act.fecha})")

        opcion = input("¿Desea eliminar todas las actividades pasadas? (si/no): ").lower()
        match opcion:
            case "si":
                for acti in actividades_pasadas:
                    del self.actividades[acti.ID]
                print(f"Se eliminaron {len(actividades_pasadas)} actividades pasadas.")
            case _:
                print("No se eliminó ninguna actividad."


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

        
gestor_actividades = Actividades()

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
            nueva_actividad = False
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
                    print("----------CATEGORIA DE ACTIVIDAD NO VALIDA----------")
                    print("----------UNICAMENTE EXISTEN (CLASE-EXAMEN-TAREA-REUNION-EVENTO)----------")

            if nueva_actividad:
                        gestor_actividades.agregar_actividad(nueva_actividad)


        case "2":
            print("---LISTAR ACTIVIDADES---")
            # opcion 2, listar actividades guardadas
            tipo_filtro = input(f"ENLISTAR ACTIVIDADES EXISTENTES POR FILTRO: (dia/semana/categoria): ").lower()
            valor = ""
            if tipo_filtro == 'categoria':
                valor = input("Introduce la categoría para buscar: ")
            gestor_actividades.listar_por_filtro(tipo_filtro, valor)
            print(gestor_actividades.listar_por_filtro(tipo_filtro,valor))
            '''
            El código de la función listar_por_filtro utiliza condicionales if/elif para verificar 
            que filtro se ha seleccionado y luego recorre el diccionario de actividades para encontrar las coincidencias y mostrarlas
            En resumen es una manera de enlistar unicamente las actividades que el usuario desee
            enlistando LAS ACTIVIDADES GUARDADOS EN EL DICCIONARIO PRO: examenes, tareas, reuniones, eventos unicamente 
            los que el quiera sin necesidad de desplegar todas y que sea desordenado
            '''
            
        case "3":
            print("---BUSCAR POR PALABRAS---")
            gestor_actividades.buscar_por_palabra()


        case "4":
            print("---ELIMINAR ACTIVIDAD---")
            gestor_actividades.eliminar_actividades_pasada()

        case "5":
            print("Saliendo del programa...")
            break
        case _:
            print("Opcion no valida...")

