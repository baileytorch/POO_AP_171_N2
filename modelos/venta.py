from cliente import Cliente
from libro import Libro


class Venta():
    def __init__(self, id_venta, cliente: Cliente, libros: Libro, total):
        self.id_venta = id_venta
        # self.cliente = client
        self.libros = list[Libro]
        self.total = total

    def agregar_libro(self):
        pass

    def calcular_total(self):
        pass

    def mostrar_detalle(self):
        pass

    def menu_venta(self):
        opc = int(input("""
        1. Agregar Libro
        2. Calcular Total
        3. Mostrar Detalle

        Ingrese Opcion:     """))

        if opc == 1:
            self.agregar_libro()
        elif opc == 2:
            self.calcular_total()
        elif opc == 3:
            self.mostrar_detalle()
