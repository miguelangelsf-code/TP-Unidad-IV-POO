# Ejercicio 9.  Turnos de un consultorio 

class Turno:
    def __init__(self, paciente, hora):
        self.paciente = paciente
        self.hora = hora
        self.estado = "pendiente"

    def marcar_atendido(self):
        self.estado = "atendido"

    def __str__(self):
        return f"{self.hora} - {self.paciente} - {self.estado}"


class Agenda:
    def __init__(self):
        self.turnos = []

    def agregar_turno(self, turno):
        self.turnos.append(turno)

    def listar_pendientes(self):
        print("TURNOS PENDIENTES")

        for turno in self.turnos:
            if turno.estado == "pendiente":
                print(turno)


turno1 = Turno("Miguel Salinas", "08:00")
turno2 = Turno("Axel Medina", "09:00")
turno3 = Turno("Jorge Rolón", "10:00")

agenda = Agenda()

agenda.agregar_turno(turno1)
agenda.agregar_turno(turno2)
agenda.agregar_turno(turno3)

turno1.marcar_atendido()
turno3.marcar_atendido()

print("TODOS LOS TURNOS")
for turno in agenda.turnos:
    print(turno)

print("\nTURNOS ATENDIDOS")
for turno in agenda.turnos:
    if turno.estado == "atendido":
        print(turno)

print("\nTURNOS PENDIENTES")
agenda.listar_pendientes()