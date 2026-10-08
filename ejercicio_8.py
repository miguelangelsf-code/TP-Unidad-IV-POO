# Ejercicio 8.  Reproductor de lista de canciones 

class Cancion:
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.duracion} minutos)"


class ListaReproduccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def duracion_total(self):
        total = 0

        for cancion in self.canciones:
            total += cancion.duracion

        return total

    def mostrar_lista(self):
        print(f"Lista: {self.nombre}")

        for cancion in self.canciones:
            print(cancion)

        print(f"Duración total: {self.duracion_total()} minutos")


cancion1 = Cancion("Por Mil Noches", "Airbag", 4.43)
cancion2 = Cancion("Rosa Pastel", "Balenova", 3.05)
cancion3 = Cancion("Sistema Solar", "Kchiporros", 3.41)

lista = ListaReproduccion("Mis canciones")

lista.agregar_cancion(cancion1)
lista.agregar_cancion(cancion2)
lista.agregar_cancion(cancion3)

lista.mostrar_lista()