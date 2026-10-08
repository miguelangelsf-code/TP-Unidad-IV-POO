# Ejercicio 10.  Carrito de compras de un e-commerce 

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - {self.precio} Gs."


class Item:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self):
        return self.producto.precio * self.cantidad


class Carrito:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)

    def calcular_total(self):
        total = 0

        for item in self.items:
            total += item.subtotal()

        return total

    def mostrar_detalle(self):
        print("DETALLE DE LA COMPRA")

        for item in self.items:
            print(
                f"{item.producto.nombre} - "
                f"Cantidad: {item.cantidad} - "
                f"Subtotal: {item.subtotal()} Gs."
            )

        print(f"Total general: {self.calcular_total()} Gs.")


producto1 = Producto("Maíz", 8000)
producto2 = Producto("CocaCola", 12000)
producto3 = Producto("Leche", 7000)

item1 = Item(producto1, 2)
item2 = Item(producto2, 1)
item3 = Item(producto3, 3)

carrito = Carrito()

carrito.agregar_item(item1)
carrito.agregar_item(item2)
carrito.agregar_item(item3)

carrito.mostrar_detalle()