def contar_lineas(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
        return len(lineas)
    except FileNotFoundError:
        return 0
print(contar_lineas("nombre.txt"))
print(contar_lineas("no_existe.txt"))
