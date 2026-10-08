# Ejercicio 13.  Habitación de un hotel 

class Habitacion:
    def __init__(self, numero, tipo, tarifa):
        self.numero = numero
        self.tipo = tipo
        self.tarifa = tarifa
        self.ocupada = False

    def ocupar(self):
        if not self.ocupada:
            self.ocupada = True
            return True

        return False

    def liberar(self):
        self.ocupada = False

    def calcular_costo(self, noches):
        return self.tarifa * noches

    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Libre"

        return (
            f"Habitación: {self.numero}\n"
            f"Tipo: {self.tipo}\n"
            f"Tarifa: {self.tarifa} Gs.\n"
            f"Estado: {estado}"
        )


numero = input("Número de habitación: ")
tipo = input("Tipo de habitación: ")
tarifa = float(input("Tarifa por noche: "))

habitacion = Habitacion(numero, tipo, tarifa)

print("\nESTADO INICIAL")
print(habitacion)

print("\nIntentando ocupar la habitación...")

if habitacion.ocupar():
    print("Habitación ocupada correctamente.")
else:
    print("La habitación ya está ocupada.")

print(habitacion)

noches = int(input("\n¿Cuántas noches desea reservar? "))

print(f"Costo de la estadía: {habitacion.calcular_costo(noches)} Gs.")

print("\nLiberando habitación...")
habitacion.liberar()

print(habitacion)