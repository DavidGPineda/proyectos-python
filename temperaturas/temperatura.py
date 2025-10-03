# print("=== Conversor de Temperaturas ===")
# print("De Celsius a Fahrenheit")
# print("De Fahrenheit a Kelvin")

# # Pedimos los datos
# celcius = float(input("grados celcius a fahrenheit: "))
# fahren = float(input("grados fahrenheit a kelvin: "))


# def grados_c(c):
#     resultado = (c * 9/5) + 32
#     return resultado


# def grados_f(f):
#     resultado = (f - 32) * 5/9 + 273.15
#     return resultado


# print(f"{celcius} Celcius = {grados_c(celcius)} Fahrenheit")
# print(f"{fahren} Fahrenheit = {grados_f(fahren)} Kelvin")

print("=== Conversor de Temperaturas ===")


def celcius_a_fahrenheit(celsius):
    """
    Convierte grados Celsius a Fahrenheit.

    Parámetros:
        c (float): temperatura en grados Celsius.

    Retorna:
        float: temperatura equivalente en Fahrenheit.
    """
    return (celsius * 9/5) + 32


def fahrenheit_a_kelvin(fahrenheit):
    """
    Convierte grados Fahrenheit a Kelvin.
    Parámetros:
        f (float): temperatra en grados Fahrenheit.
    Retorna:
        float: Temperatura equivalente a Kelvin.
    """
    return (fahrenheit - 32) * 5/9 + 273.15


while True:
    print("\nOpciones: ")
    print("1. Convertir Celcius a Fahrenheit")
    print("2. Convertir Fahrenheit a Kelvin")
    print("3. Salir")

    opcion = input("Elige una opción (1/2/3)")

    if opcion == "1":
        c = float(input("Ingresa grados Celcius: "))
        print(f"{c} °C = {celcius_a_fahrenheit(c)} °F")
    elif opcion == "2":
        f = float(input("Ingresa grados Fahrenheit: "))
        print(f"{f} °F = {fahrenheit_a_kelvin(f)} °K")
    elif opcion == "3":
        print("Hasta luego")
        break
    else:
        print("Opcion no valida, intenta de nuevo.")
