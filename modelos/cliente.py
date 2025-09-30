class Cliente():
    def __init__(self, rut, nombre, email, telefono):
        self.rut = rut
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def registrar_cliente(self):
        cliente = {}
        rut = input("Ingrese el rut del cliente: ")
        nombre = input("Ingrese el nombre del cliente: ")
        email = input("Ingrese el email del cliente: ")
        telefono = input("Ingrese el telefono del cliente: ")

        cliente["rut"] = rut
        cliente["nombre"] = nombre
        cliente["email"] = email
        cliente["telefono"] = telefono

        print(cliente)

    def mostrar_info(self):
        print(f"""Nombre cliente: {self.nombre}
            Rut cliente: {self.rut}
            Email cliente: {self.email}
            Teléfono cliente: {self.telefono}""")

    def actualizar_email(self):
        cliente = {}
        email = input("Ingrese el email del cliente: ")
        cliente["email"] = email

    def actualizar_telefono(self):
        cliente = {}
        telefono = input("Ingrese el telefono del cliente: ")
        cliente["telefono"] = telefono

    def menu_cliente(self):

        opc = int(input("""
        1. Registrar Cliente
        2. Actualizar Email
        3. Actualizar Telefono

        Ingrese Opcion:     """))

        if opc == 1:
            self.registrar_cliente()
        elif opc == 2:
            self.actualizar_email()
        elif opc == 3:
            self.actualizar_telefono()
