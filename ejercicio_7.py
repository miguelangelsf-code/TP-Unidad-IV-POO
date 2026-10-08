# Ejercicio 7.  Control de stock con alertas 

class ProductoStock:
    def __init__(self, nombre, stock, stock_minimo):
        self.nombre = nombre
        self.stock = stock
        self.stock_minimo = stock_minimo

    def ingresar_mercaderia(self, cantidad):
        if cantidad > 0:
            self.stock += cantidad
            print(f"Ingresaron {cantidad} unidades.")
            self.verificar_stock()
        else:
            print("La cantidad debe ser positiva.")

    def registrar_venta(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser positiva.")
        elif cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Venta registrada: {cantidad} unidades.")
            self.verificar_stock()
        else:
            print("Venta rechazada: no hay suficiente stock.")

    def verificar_stock(self):
        if self.stock < self.stock_minimo:
            print("ALERTA: el stock está por debajo del mínimo.")

    def __str__(self):
        return f"Producto: {self.nombre} | Stock: {self.stock} | Stock mínimo: {self.stock_minimo}"


producto = ProductoStock("Yerba Mate", 20, 10)

print(producto)

producto.registrar_venta(8)
print(producto)

producto.registrar_venta(5)
print(producto)

producto.ingresar_mercaderia(15)
print(producto)