class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def actualizar_precio(self, nuevo_precio):
        try:
            valor = float(nuevo_precio)
            if valor >= 0.0:
                self.precio = valor
            else:
                print("Favor de ingresar un valor mayor a 0.0")
        except ValueError:
            print("El precio debe ser un número")
    
    def actualizar_cantidad(self, nueva_cantidad):
        try:
            valor = int(nueva_cantidad)
            if valor >= 0:
                self.cantidad = valor
            else:
                print("Favor de ingresar un valor mayor a 0")
        except ValueError:
            print("La cantidad debe ser un número")
    
    def calcular_valor_total(self):
        return self.precio * self.cantidad
    
    def __str__(self):
        return f"Producto: {self.nombre} (${self.precio:.2f}) disponibles: {self.cantidad}"

class Inventario:
    def __init__(self):
        self.productos = []
        
    def agregar_producto(self, producto):
        """
        Añade un objeto Producto a la colección.
        Aplica el principio de composición "tiene un".
        """
        # Validación básica: verificar que sea una instancia de Producto [10, 11]
        if isinstance(producto, Producto):
            self.productos.append(producto)
            print(f"Éxito: {producto.nombre} (${producto.precio}) cantidad: {producto.cantidad} añadido al inventario.")
        else:
            raise TypeError("Solo se pueden añadir objetos de tipo Producto")
    
    def buscar_producto(self, nombre=''):
        try:
            valor = str(nombre)
            for producto in self.productos:
                if valor.lower() == producto.nombre.lower():
                    return producto
            return None
        except ValueError:
            print("Ingrese el nombre del producto a buscar")
        
    def calcular_valor_inventario(self):
        total = 0.0
        for producto in self.productos:
            total += producto.calcular_valor_total()
        return total
    
    def listar_productos(self):
        for producto in self.productos:
            print(producto)
    
def menu_principal(mi_inventario):
    
    while True:
        print("Elija una opción del menu ingresando el número correspondiente")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")
        
        try:
            opcion = int(input("Ingrese su opción elejida por favor: "))
            match opcion:
                case 1:
                    # Validar la entrada del nombre del producto
                    while True:
                        try:
                            nombre = str(input("Ingrese el nombre del producto: "))
                            break
                        except ValueError:
                            print("Ingrese el texto del nombre")
                    
                    # Validar la entrada del precio del producto
                    while True:
                        try:
                            precio = float(input("Ingrese el precio del producto: "))
                            if precio < 0.0:
                                print("Ingrese un valor mayor a 0.0")
                            else:
                                break
                        except ValueError:
                            print("Ingrese un valor mayor a 0.0")
                            
                    # Validar la entrada de la cantidad del producto
                    while True:
                        try:
                            cantidad = int(input("Ingrese la cantidad de existencia del producto: "))
                            if cantidad < 0:
                                print("Ingrese un valor mayor a 0")
                            else:
                                break
                        except ValueError:
                            print("Ingrese un valor mayor a 0")
                    
                    # Instanciamos el objeto Producto hasta tener valores válidos
                    mi_producto = Producto(nombre, precio, cantidad)
                    mi_inventario.agregar_producto(mi_producto)
                case 2:
                    busqueda = input("Ingrese el nombre del producto a buscar: ")
                    print(mi_inventario.buscar_producto(busqueda))
                case 3:
                    mi_inventario.listar_productos()
                case 4:
                    print(f"El valor total del inventario es $ {mi_inventario.calcular_valor_inventario()}")
                case 5:
                    break
                case _:
                    print ("Ingrese el número de una opción válida por favor.")
        except ValueError:
            print ("Ingrese el número de una opción válida por favor.")

if __name__ == "__main__":
    mi_inventario = Inventario()
    print("Bienvenido al sistema básico para gestionar productos y realizar operaciones de inventario.")
    menu_principal(mi_inventario)
    