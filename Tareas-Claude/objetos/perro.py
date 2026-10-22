class perro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 100
    def caminar(self):
        self.energia -= 10
        return self.energia
    def descansar(self):
        self.energia = min(self.energia + 20, 100)
        return self.energia

perro1 = perro("milo")
perro2 = perro("lori")

print(perro1.caminar())
print(perro1.caminar())
print(perro1.caminar())
print(perro2.caminar())
print(perro2.descansar())