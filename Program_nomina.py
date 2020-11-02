import csv
import os


def guardar_archivo(extension, campos):
        guardar="si"
        lista_empleados = []
        nombre_archivo = input(f"Ingrese nombre del archivo agregando al final .csv ")

        modo = "a" # para ver los tipos de modos sobre escritura o agregar informaciòn
        if os.path.isfile(nombre_archivo):
            respuesta = input("\n El archivo ya existe desea sobreescribirlo? Si/No : ").lower()
            if respuesta == "si":
                modo = 'w'
 
        while guardar == "si":
            empleado = {}
            for campo in campos:
                empleado[campo] = input(f"Ingrese {campo} del empleado ")
                print(campo)
                if campo == campos[0] or campo ==campos[3]:
                   print(campo)
                   empleado[campo]= verific_dato(campo, empleado[campo])
            lista_empleados.append(empleado)      
            guardar = input("\n Desea seguir agregando empleados? Si/No : ")
        
        try:
            with open(nombre_archivo, modo, newline = '') as file:
                file_guarda =  csv.DictWriter(file, fieldnames=campos)
                file_guarda.writeheader()
                file_guarda.writerows(lista_empleados)
                
                #verificar si el archivo esta creado
                # verific_creacion_archivo():
                print("\n Se guardo correctamente el archivo   ")
                return
                
        except IOError:
            print("\n Ocurrrio un error en el archivo  ")

def verific_dato(campo, valor):
    while not valor.isdigit():
        valor=input(f'\n No es un valor valido, colocar un {campo}')
    return valor


def leer_archiv_csv(archivo):
    lista = []
    try:
        with open(archivo, 'r', newline='') as file:
            lectura_csv = csv.DictReader(file)
            for linea in lectura_csv:
                lista.append(linea)
    except IOError:
        print("\n Ocurrrio un error en el archivo",error)
    
    return lista




# def verific_creacion_archivo(archivo):

def _menu_():#1 menu punto a
    
    extension = ".csv "
    vacaciones = "Vacaciones_dias.csv"
    campos = ['Legajo',  'Apellido',  'Nombre', 'Total Vacaciones']
    while True:
        print("\n\nElija una opción  \n 1. Ingresar Nuevo Empleado \n 2. Dias disponibles de vacaciones para empleado \n 3. Salir")
        opcion= input("")
        
        if opcion == "3":
            exit()
       
        if opcion == "1":
           guardar_archivo(extension, campos)
           
        #comprobar archivo si antes estaba creado o no
        # if opcion == "2":
        #     ejer7_cargar(archivo)
        else:
            print("\n Por favor elija una opcion valida")
_menu_()
