# def agregar_nombre(ruta, nombre):
#     try:
#         with open(ruta, "a", encoding="utf-8") as archivo:
#             archivo.write(f"{nombre}\n")
#             print(f"{nombre}")
#         return nombre
#     except FileNotFoundError:
#         print("archivo no encontrado")
# def contar_lineas(ruta):
#     try:
#         with open(ruta, "r", encoding="utf-8") as archivo:
#             lineas = archivo.readlines()
#             for linea in lineas:
#                 print(linea.strip())
#         return len(lineas)
#     except FileNotFoundError:
#         return 0

# def nombrar_contar(ruta, nombre):
#     agregar_nombre(ruta, nombre)
#     completo = contar_lineas(ruta)
#     return completo

# print(nombrar_contar("nombre.txt", "milo"))

def contar_lineas(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
        return len(lineas)
    except FileNotFoundError:
        return 0

def agregar_nombre(ruta, nombre):
    with open(ruta, "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre}\n")
    return contar_lineas(ruta)

print(agregar_nombre("nombres.txt", "ana"))
print(agregar_nombre("nombres.txt", "luis"))