print("=== Calculadora simple ===")
print("Escribe 'salir' en la operación para terminar.\n")

while True:
    # Pedimos los números
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    # Pedimos la operación
    print("Operaciones: +  -  *  /")
    operacion = input("Elige una operación: ")

    if operacion.lower() == "salir":
        print("¡Gracias por usar la calculadora!")
        break

    if operacion == "+":
        resultado = num1 + num2
    elif operacion == "-":
        resultado = num1 - num2
    elif operacion == "*":
        resultado = num1 * num2
    elif operacion == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Error: división por cero"
    else:
        resultado = "Operación no válida"

    print("Resultado:", resultado, "\n")
