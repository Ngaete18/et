import random
import csv

# Datos de los trabajadores
trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez",
                "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", 
                "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

# Variable global para los sueldos
sueldos = []

# Función para generar sueldos aleatorios
def generar_sueldos():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]

# Función para clasificar sueldos
def clasificar_sueldos():
    global sueldos
    menores_800k = []
    entre_800k_2m = []
    mayores_2m = []

    for i, sueldo in enumerate(sueldos):
        nombre = trabajadores[i]
        if sueldo < 800000:
            menores_800k.append((nombre, sueldo))
        elif 800000 <= sueldo <= 2000000:
            entre_800k_2m.append((nombre, sueldo))
        else:
            mayores_2m.append((nombre, sueldo))
    
    # Mostrar clasificación
    print("\nSueldos menores a $800.000 - TOTAL:", len(menores_800k))
    print("{:<20} {:<15}".format("Nombre empleado", "Sueldo"))
    for empleado in menores_800k:
        print("{:<20} ${:<15,.2f}".format(empleado[0], empleado[1]))

    print("\nSueldos entre $800.000 y $2.000.000 - TOTAL:", len(entre_800k_2m))
    print("{:<20} {:<15}".format("Nombre empleado", "Sueldo"))
    for empleado in entre_800k_2m:
        print("{:<20} ${:<15,.2f}".format(empleado[0], empleado[1]))

    print("\nSueldos superiores a $2.000.000 - TOTAL:", len(mayores_2m))
    print("{:<20} {:<15}".format("Nombre empleado", "Sueldo"))
    for empleado in mayores_2m:
        print("{:<20} ${:<15,.2f}".format(empleado[0], empleado[1]))

# Función para calcular estadísticas
def calcular_estadisticas():
    if not sueldos:
        print("Aún no se han generado los sueldos.")
        return
    
    sueldo_maximo = max(sueldos)
    sueldo_minimo = min(sueldos)
    promedio_sueldos = sum(sueldos) / len(sueldos)

    # Calcular media geométrica
    media_geometrica = 1
    for sueldo in sueldos:
        media_geometrica *= sueldo
    media_geometrica **= (1 / len(sueldos))

    print("\nEstadísticas de Sueldos:")
    print(f"Sueldo más alto: ${sueldo_maximo}")
    print(f"Sueldo más bajo: ${sueldo_minimo}")
    print(f"Promedio de sueldos: ${promedio_sueldos:.2f}")
    print(f"Media geométrica de sueldos: ${media_geometrica:.2f}")

# Función para generar reporte de sueldos
def generar_reporte():
    if not sueldos:
        print("Aún no se han generado los sueldos.")
        return
    
    print("\nReporte de Sueldos:")
    print("{:<20} {:<15} {:<15} {:<15} {:<15}".format("Nombre empleado", "Sueldo Base", 
                                                    "Descuento Salud", "Descuento AFP", "Sueldo Líquido"))
    for i, sueldo in enumerate(sueldos):
        nombre = trabajadores[i]
        desc_salud = sueldo * 0.07
        desc_afp = sueldo * 0.12
        sueldo_liquido = sueldo - desc_salud - desc_afp
        print("{:<20} ${:<14,.2f} ${:<14,.2f} ${:<14,.2f} ${:<14,.2f}".format(nombre, sueldo, desc_salud, desc_afp, sueldo_liquido))

    # Exportar a CSV
    with open('reporte_sueldos.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        csv_writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        for i, sueldo in enumerate(sueldos):
            nombre = trabajadores[i]
            desc_salud = sueldo * 0.07
            desc_afp = sueldo * 0.12
            sueldo_liquido = sueldo - desc_salud - desc_afp
            csv_writer.writerow([nombre, sueldo, desc_salud, desc_afp, sueldo_liquido])

# Función principal del programa
def main():
    while True:
        print("\nBienvenido al sistema de gestión de sueldos de la empresa:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            generar_sueldos()
            print("Sueldos aleatorios asignados exitosamente.")
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            calcular_estadisticas()
        elif opcion == '4':
            generar_reporte()
            print("Reporte de sueldos generado y exportado a reporte_sueldos.csv")
        elif opcion == '5':
            print("¡Hasta luego!")
            print("desarrollado por nicolas gaete")
            print("21.923.612-3")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida (1-5).")

main()