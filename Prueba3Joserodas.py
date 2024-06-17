import csv
import os
from datetime import datetime

def registrar_reclamo(reclamos):
    rut = input("Ingrese RUT del reclamante (con DV): ")
    monto = float(input("Ingrese monto de la compra en miles de pesos: "))
    reclamo = input("Ingrese reseña del reclamo (maximo 20 caracteres): ")

    if len(reclamo) > 20:
        print("Error la reseña debe tener un maximo 20 caracteres.")
        return

    fecha = datetime.now().strftime("%d-%m-%Y")
    reclamos.append((rut, fecha, monto, reclamo))
    print("Reclamo registrado exitosamente.")

def listar_reclamos(reclamos):
    print("\nListado de reclamos:")
    if not reclamos:
        print("No hay reclamos registrados.")
    else:
        print("\nListado de reclamos:")
    for i in range(len(reclamos)):
        rut, fecha, monto, descripcion = reclamos[i]
        print(f"{i+1}. Fecha: {fecha}, RUT: {rut}, monto: {monto} miles de pesos, reclamo: {descripcion}")


def respaldar_reclamos(reclamos):
    if not reclamos:
        print("No hay reclamos para respaldar.")
        return

    nombre_archivo = 'respaldo_reclamos.csv'
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['RUT', 'fecha', 'monto', 'reclamo'])
        writer.writerows(reclamos)
    print(f"Reclamos respaldados en {nombre_archivo}.")

def menu_inicial():
    reclamos = [ ]
    while True:
        print("-----Menu de opciones -----\n1.Registrar Reclamo\n2.Listar Reclamos\n3.Respaldar Reclamos\n4.Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            registrar_reclamo(reclamos)
        elif opcion == '2':
            listar_reclamos(reclamos)
        elif opcion == '3':
            respaldar_reclamos(reclamos)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida intente nuevamente.")

if __name__ == "__main__":
    menu_inicial()
