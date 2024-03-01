#Menu de cuentas bancArias
class CuentaBancaria():
    def __init__ (self, titular, saldo, nroCuenta):
        self.titular = titular
        self.saldo = saldo
        self.nroCuenta = nroCuenta
    def consultarSaldo(self):
        print("su saldo es ", self.saldo)
    def retirar (self,cantidad):
        if cantidad<=self.saldo:
            self.saldo-=cantidad
            print("retirado",cantidad)
            self.consultarSaldo()
        else:
            print("su saldo es insuficiente")
    def depositar (self, cantidad):
        self.saldo += cantidad
        self.consultarSaldo()

    def transferir (self, cantidad, receptor):
        if cantidad<= self.saldo:
            self.saldo-=cantidad
            receptor.saldo += cantidad
            print("Transferido", cantidad)
            self.consultarSaldo()
            receptor.consultarSaldo()
        else:
            
            print("saldo insuficiente")

def registrar_cuenta ( titular, cedula):
    cuenta = CuentaBancaria ( titular, 0, len(Cuentas))
    Cuentas.append(cuenta)

Cuentas = []
def menu_principal ():
    print ("""
           1. Registrar Nueva Cuenta
           2. Iniciar Sesion en Cuenta
           3. Salir
           """)
    opc = int (input( "Ingrese la Opcion: "))
    if opc == 1:
        titular = input ("Ingresar el Nombre: ")
        cedula = input ( "Ingresa Cedual: ")
        registrar_cuenta ( titular, cedula)
    elif opc == 2: 
        nro_cuenta = int (input("Ingrese su Numero de Cuenta: "))
        if nro_cuenta > len (Cuentas):
            print ( "El Numero de cuenta no existe")
        else:
            print ("Ingreso Exitoso")
            menu_usuario (nro_cuenta)
    elif opc == 3:
        exit()
    menu_principal()

def menu_usuario (nro_cuenta):
    Cuenta = Cuentas [nro_cuenta]
    print ("Bienvenido", Cuenta.titular)
    print("""
          1. Depositar
          2. Transferir
          3. Consultar
          4. Regresar
          """)
    opc = int(input("Ingresar opcion: "))
    if opc == 1:
        cantidad = int(input("Que Cantidad quieres Depositar: "))
        Cuenta.depositar()
    elif opc == 2:
        nro_cuenta_transferir = int(input("Ingresa el Numero de cuenta a transferir: "))
        Cuenta_transferir = Cuenta [nro_cuenta_transferir]
        Cuenta.transferir ( Cuenta_transferir)

menu_principal()