# Ejercicio 2.  Producto de almacén 

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def valor_total_stock(self):
        return self.precio * self.stock

    def __str__(self):
        return f"Producto: {self.nombre}\nPrecio: {self.precio} Gs.\nStock: {self.stock}"


producto1 = Producto("Harina leudante", 9000, 30)
producto2 = Producto("Fideo Monarca", 7000, 25)
producto3 = Producto("Sal ", 5000, 20)

print(producto1)
print(f"Valor total en stock: {producto1.valor_total_stock()} Gs.\n")

print(producto2)
print(f"Valor total en stock: {producto2.valor_total_stock()} Gs.\n")

print(producto3)
print(f"Valor total en stock: {producto3.valor_total_stock()} Gs.")