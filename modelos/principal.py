from cliente import Cliente
from venta import Venta
from libro import Libro
from libreria import Libreria


class Principal:
    def menu_principal(self):
        while True:
            opc = int(input("""
            1. Opciones Cliente
            2. Opciones Venta
            3. Opciones Libro
            4. Opciones Libreria
            5. Salir

            Ingrese Opcion:     """))

            if opc == 1:
                obj = Cliente("11-1", "user", "user@email.cl", 784512)
                obj.menu_cliente()
            elif opc == 2:
                obj_cliente = Cliente("11-1", "user", "user@email.cl", 784512)
                lista_libros = Libro('LI01', 'Titulo Libro',
                                     'Autor Libro', 4500, 10)
                obj = Venta(1, obj_cliente, lista_libros, 45000)
                obj.menu_venta()
            elif opc == 3:
                obj = Libro("1111", "libro de prueba",
                            "autor de prueba", 152000, 10)
                obj.menu_libro()
            elif opc == 4:
                pass
                # menu_libreria()
            elif opc == 5:
                break


obj = Principal()
obj.menu_principal()
