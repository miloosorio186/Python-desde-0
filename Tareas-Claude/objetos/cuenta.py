class Cuenta:
    def __init__(self):
        self.saldo = 0
    def depositar(self, monto):
        self.saldo = self.saldo + monto
        return self.saldo
    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo = self.saldo - monto
        return self.saldo


c = Cuenta()
print(c.depositar(500))   # 500
print(c.retirar(800))     # 500 (no alcanza, no cambia)
print(c.retirar(200))     # 300
