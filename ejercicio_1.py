# Ficha de cliente

class Cliente:
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre}\nCédula: {self.cedula}\nTeléfono: {self.telefono}"


cliente1 = Cliente("Juan Pérez", "4.567.890", "0981 123456")
cliente2 = Cliente("María González", "5.678.901", "0972 654321")

print("FICHA DEL CLIENTE")
print(cliente1)

print("\nFICHA DEL CLIENTE")
print(cliente2)