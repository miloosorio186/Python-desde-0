class Vehiculo:
    def __init__(self, marca):  
        self.marca = marca
        self.velocidad = 0
    def acelerar(self, cantidad):
        self.velocidad = cantidad + self.velocidad
        return self.velocidad

class moto(Vehiculo):
    def __init__(self, marca, cilindraje):
        super().__init__(marca)
        self.cilindraje = cilindraje
    

        
moto_test = moto("yamaha", 150)
print(moto_test.acelerar(30))
print(moto_test.acelerar(20))