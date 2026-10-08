# Ejercicio 6.  Caja registradora de una cuenta corriente 

class CuentaCorriente:
    def __init__(self, cliente, saldo=0):
        self.cliente = cliente
        self.saldo = saldo

    def acreditar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Se acreditaron {monto} Gs.")
        else:
            print("El monto a acreditar debe ser positivo.")

    def registrar_consumo(self, monto):
        if monto <= 0:
            print("El consumo debe ser positivo.")
        elif monto <= self.saldo:
            self.saldo -= monto
            print(f"Compra registrada por {monto} Gs.")
        else:
            print("Compra rechazada: saldo insuficiente.")

    def __str__(self):
        return f"Cliente: {self.cliente} | Saldo: {self.saldo} Gs."


cuenta = CuentaCorriente("Miguel Salinas")

print(cuenta)

cuenta.acreditar(200000)
print(cuenta)

cuenta.registrar_consumo(80000)
print(cuenta)

cuenta.registrar_consumo(150000)
print(cuenta)

cuenta.acreditar(100000)
print(cuenta)

cuenta.registrar_consumo(150000)
print(cuenta)