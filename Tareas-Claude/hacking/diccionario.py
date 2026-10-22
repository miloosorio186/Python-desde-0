fallos = {}
betados = []
while True:
    try:
        diccionario = input("dame el nombre del el archivo logs: ")
        with open(diccionario, "r", encoding="utf-8") as archivo:
            datos = archivo.readlines()
            for i in datos: 
                partes = i.strip().split()
                if len(partes) < 4:
                    continue
                if partes[2] == "FALLIDO":
                    nombre = partes[3]
                    fallos[nombre] = fallos.get(nombre, 0) + 1 
            for usuarios, cantidad in fallos.items():
                if cantidad >= 3:
                    betados.append(usuarios)
                    print(f"ALERTA: {usuarios} tiene 3 fallos")
                            
      
        break
    except FileNotFoundError:
        print("no se encontro el archivo")


print(fallos)

