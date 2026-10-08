# Ejercicio 3.  Empleado y su sueldo 

class Empleado:
    def __init__(self, nombre, cargo, salario_mensual):
        self.nombre = nombre
        self.cargo = cargo
        self.salario_mensual = salario_mensual

    def salario_anual(self):
        return self.salario_mensual * 13

    def __str__(self):
        return f"Nombre: {self.nombre}\nCargo: {self.cargo}\nSalario mensual: {self.salario_mensual} Gs."


empleado1 = Empleado("Miguel Salinas", "Vendedor", 3700000)
empleado2 = Empleado("Axel Medina", "Administradora", 4700000)

print(empleado1)
print(f"Salario anual con aguinaldo: {empleado1.salario_anual()} Gs.\n")

print(empleado2)
print(f"Salario anual con aguinaldo: {empleado2.salario_anual()} Gs.")