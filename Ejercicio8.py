class Persona:
    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.__cantidad = cantidad

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad

    def mostrar(self):
        print("Titular:", self.titular.nombre)
        print("DNI del titular:", self.titular.dni)
        print("Cantidad:", self.__cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        self.__cantidad -= cantidad

class CuentaJoven(Cuenta):
    def __init__(self, titular, bonificacion, cantidad=0.0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    def get_bonificacion(self):
        return self.__bonificacion

    def es_titular_valido(self):
        edad = self.titular.edad
        return 18 <= edad <= 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("Retiro no permitido para titulares no válidos")

    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print("Bonificación:", self.__bonificacion, "%")  # Mostrar la bonificación como porcentaje

nombre_titular = input("Ingresar el nombre del titular: ")
dni_titular = input("Ingresar el DNI del titular: ")
edad_titular = int(input("Ingresar la edad del titular: "))
bonificacion = float(input("Ingresar la bonificación en porcentaje: "))

titular = Persona(nombre_titular, dni_titular, edad_titular)
cuenta_joven = CuentaJoven(titular, bonificacion)
cuenta_joven.mostrar()

cantidad_ingreso = float(input("Ingresar la cantidad a ingresar: "))
cuenta_joven.ingresar(cantidad_ingreso)

retiro_valido = cuenta_joven.es_titular_valido()
print("¿Titular válido?", "VERDADERO" if retiro_valido else "FALSO")

if retiro_valido:
    cantidad_retiro = None
    while cantidad_retiro is None:
        try:
            cantidad_retiro = float(input("Ingresar la cantidad a retirar: "))
        except ValueError:
            print("Cantidad inválida. Ingrese un número válido.")
    cuenta_joven.retirar(cantidad_retiro)
else:
    print("Operación de retiro no permitida para titulares no válidos")

cuenta_joven.mostrar()