import csv
import os


def guardar_archivo(extension, campos):
        guardar="si"
        lista_empleados = []
        nombre_archivo = input(f"Ingrese nombre del archivo agregando al final .csv ")

        modo = "a" # para ver los tipos de modos sobre escritura o agregar informaciòn
        exite = False

        if os.path.isfile(nombre_archivo):
            respuesta = input("\n El archivo ya existe desea sobreescribirlo? Si/No : ").lower()
            if respuesta == "si":
                modo = 'w'
            else:
                exite = True
        while guardar == "si":
            empleado = {}
            for campo in campos:
                empleado[campo] = input(f"Ingrese {campo} del empleado ")
                if campo == campos[0] or campo ==campos[3]:
                   empleado[campo]= verific_dato(campo, empleado[campo])
            lista_empleados.append(empleado)      
            guardar = input("\n Desea seguir agregando empleados? Si/No : ")
        
        try:
            with open(nombre_archivo, modo, newline = '') as file:
                file_guarda =  csv.DictWriter(file, fieldnames=campos)
                if not exite:
                    file_guarda.writeheader()
                file_guarda.writerows(lista_empleados)
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


def contar_dias(legajo, vacacciones):
    contador = 0
    for vacacion in vacacciones:
        if legajo == vacacion['Legajo']: 
            contador = contador + 1
    return contador
    

def mostrar_vacaciones(archiv_vacaciones):
    vacaciones = leer_archiv_csv(archiv_vacaciones)
    respuesta= input("Ingrese legajo del empleado ")
    legajo = verific_dato("Legajo",respuesta)
    dias = contar_dias(legajo, vacaciones)
    archiv_emplead = input("Ingrese el nombre del archivo:  " )
    empleados = leer_archiv_csv(archiv_emplead)
    for empleado in empleados:
        if legajo == empleado['Legajo']:
            print(f'Legajo {empleado["Legajo"]}, {empleado["Nombre"]} {empleado["Apellido"] }, le restan {int(empleado["Total Vacaciones"]) - dias } días de vacaciones') 

def _menu_():#1 menu punto a
    
    extension = ".csv "
    vacaciones = "Vacaciones_dias.csv"
    campos = ['Legajo',  'Apellido',  'Nombre', 'Total Vacaciones']
    while True:
        print("\n\nElija una opción  \n 1. Ingresar Nuevo Empleado \n 2. Mostrar vacaciones del empleado \n 3. Salir")
        opcion= input("")
        
        if opcion == "3":
            exit()
       
        if opcion == "1":
           guardar_archivo(extension, campos)
           
        if opcion == "2":
            mostrar_vacaciones(vacaciones)
        else:
            print("\n Por favor elija una opcion valida")
_menu_()
