import random
print("=== Adivinar Número ===")

while True:
    print("\nAdivina el numero entre 1 al 10")

    try:
        num = int(input("Ingresa un número del 1 al 10: "))
    except ValueError:
        print("Número invalido, intenta de nuevo")
        continue

    if num < 1 or num > 10:
        print("Número fuera de rango, intenta entre 1 y 10")
        continue

    numAleatorio = random.randint(1, 10)

    if num == numAleatorio:
        print("Adivinaste el numero")
        print("El numero era: ", numAleatorio)
        print("Tu número fue: ", num)
    elif num > numAleatorio:
        print("Muy alto, fallaste")
        print("Tu número: ", num)
        print("El numero era: ", numAleatorio)
    else:
        print("⬇️ Muy bajo, fallaste")

    print(f"Tu número: {num}")
    print(f"Número correcto: {numAleatorio}")

    jugar = input("¿Quieres jugar otra vez? (s/n): ").lower()
    if jugar != "s":
        print("Gracias por jugar")
        break
