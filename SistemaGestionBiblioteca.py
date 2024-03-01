#Sistemas de Gestion de biblioteca
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

CuentaBancaria1=CuentaBancaria("Gabriel", 522, 5144222255666)
CuentaBancaria1.consultarSaldo()
#CuentaBancaria1=CuentaBancaria("federico", 1500, 60140080001) 
#CuentaBancaria2=CuentaBancaria("Pedro", 400, 604441115555)
#CuentaBancaria1.transferir(120,"federer")
