# print("Agenda de contactos")

# contactos: dict = {}

# while True:
#     print("Selecciona una opcion")
#     print("1. Agregar Contacto")
#     print("2. Buscar Contacto")
#     print("3. Borrar Contacto")
#     print("4. Salir")
#     print(contactos)

#     accion = input("Que accion desea realizar, (1/2/3/4): ")

#     if accion == "1":
#         nombre = input("Ingresa el nombre: ")
#         telefono = input("Ingresa el telefono: ")

#         contactos[nombre] = telefono
#     elif accion == "2":
#         nombrebuscar = input("Ingresa el nombre del contacto: ")
#         if nombrebuscar in contactos:
#             print(nombrebuscar, contactos[nombrebuscar])
#         else:
#             print("Contacto no encontrado")
#     elif accion == "3":
#         nombreborrar = input("Ingresa el contacto a borrar: ")
#         if nombreborrar in contactos:
#             del contactos[nombreborrar]
#             print("Contacto borrado: ", nombreborrar)
#         else:
#             print("Contacto no encontrado")
#     elif accion == "4":
#         print("Good-bye")
#         break
#     else:
#         print("Opcion no valida")

print("Agenda de contactos")

contactos: dict = {}


def agregar_contacto():
    nombre = input("Ingresa el nombre: ")
    telefono = input("Ingresa el teléfono: ")
    contactos[nombre] = telefono
    print(f"Contacto agregado: {nombre} -> {telefono}")


def buscar_contacto():
    nombre = input("Ingresa el nombre del contacto: ")
    if nombre in contactos:
        print(f"{nombre}: {contactos[nombre]}")
    else:
        print("Contacto no encontrado")


def borrar_contacto():
    nombre = input("Ingresa el conctacto a borrar: ")
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto borrado: {nombre}")
    else:
        print("Contacto no encontrado")


while True:
    print("\n --- Menú ---")
    print("1. Agregar Contacto")
    print("2. Buscar Contacto")
    print("3. Borrar Contacto")
    print("4. Ver Agenda")
    print("5. Salir")

    accion = input("Selecciona una opción (1/2/3/4/5): ")

    match accion:
        case "1":
            agregar_contacto()
        case "2":
            buscar_contacto()
        case "3":
            borrar_contacto()
        case "4":
            print("Agenda completa:", contactos)
        case "5":
            print("Good-bye")
            break
        case _:
            print("Opción no válida")
