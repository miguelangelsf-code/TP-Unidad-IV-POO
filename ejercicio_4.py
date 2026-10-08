# Ejercicio 4. Libro de una bliblioclas

class Libro:
    def __init__(self, titulo, autor, disponible):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def __str__(self):
        if self.disponible:
            estado = "Disponible"

        else:
            estado = "Prestado"

        return (
            f"Titulo: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Estado: {estado}"
        )
libro1 = Libro("Piensa en Python", "Allen B. Dow", True)
libro2 = Libro("Ultimate Python", "Nicolas Schurmann", False)

print("LIBRO 1")
print(libro1)

print("\nLIBRO 2")
print(libro2)