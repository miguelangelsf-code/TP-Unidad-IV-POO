# Ejercicio 5.  Vehículo de una agencia 

class Vehiculo:
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def descripcion_comercial(self):
        return f"{self.marca} | {self.modelo} | {self.año} — {self.precio:,.0f} Gs."


vehiculo1 = Vehiculo("Toyota", "Corolla", 2020, 95000000)
vehiculo2 = Vehiculo("Koenigsegg", "Agera R", 2014, 8700000000)

print("Maraca - Modelo - Año - Precio")
print(vehiculo1.descripcion_comercial())
print(vehiculo2.descripcion_comercial())