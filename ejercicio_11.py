# Ejercicio 11.  Estudiante y sus materias 

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def registrar_nota(self, materia, nota):
        self.notas.append((materia, nota))

    def calcular_promedio(self):
        if len(self.notas) == 0:
            return 0

        total = 0

        for materia, nota in self.notas:
            total += nota

        return total / len(self.notas)

    def esta_aprobado(self):
        return self.calcular_promedio() >= 7

    def mostrar_boletin(self):
        print(f"BOLETÍN DE {self.nombre}")

        for materia, nota in self.notas:
            print(f"{materia}: {nota}")

        promedio = self.calcular_promedio()

        print(f"Promedio: {promedio:.2f}")

        if self.esta_aprobado():
            print("Condición: Aprobado")
        else:
            print("Condición: No aprobado")


estudiante = Estudiante("Miguel Salinas")

estudiante.registrar_nota("Contabilidad", 100)
estudiante.registrar_nota("Matemática IV", 93)
estudiante.registrar_nota("Base de Datos", 95)
estudiante.registrar_nota("Optativo", 100)
estudiante.registrar_nota("Sistema Distribuido", 100)

estudiante.mostrar_boletin()