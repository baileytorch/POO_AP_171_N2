class Libro():
    def __init__(self, codigo, titulo, autor, precio, stock):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.stock = stock

    def registrar_libro(self):
        libros ={}
        codigo = input("Ingrese el codigo del libro: ")
        titulo = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el autor del libro: ")
        precio = input("Ingrese el precio del libro: ")
        stock = input("Ingrese el stock del libro: ")

        libros["codigo"] =codigo
        libros["titulo"] =titulo
        libros["autor"] =autor
        libros["precio"] =precio
        libros["stock"] =stock

        print(libros)
        return libros

    def libros_defecto(self):
        pass
    
    def mostrar_info(self):
        pass

    def actualizar_stock(self):
        pass

    def aplicar_descuento(self):
        pass


    def menu_libro(self):
  
        opc = int(input("""
        1. Registrar Libro
        2. Mostrar Info libro
        3. Actualizar Telefono
        4. Aplicar Descuento

        Ingrese Opcion:     """))

        if opc ==1:
            self.registrar_libro()
        elif opc==2:
            self.mostrar_info()
        elif opc ==3:
            self.actualizar_stock()
        elif opc ==4:
            self.aplicar_descuento()