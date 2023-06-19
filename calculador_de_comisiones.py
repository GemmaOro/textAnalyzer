nombre = input("Introduce tu nombre: ")
ventas = input("Introduce el numero de ventas totales mensuales: ")

ventas = int(ventas)
resultado_comisiones = round(ventas*13/100,2)

print(f"Enhorabuena {nombre} tus comisiones para este mes son {resultado_comisiones}")

