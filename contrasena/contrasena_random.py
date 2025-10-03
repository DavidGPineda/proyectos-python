import random
import string

print(" === Contraseña Aleatoria ===")


while True:
    print("¡Desea una contraseña aleatoria?")
    print("1. Si")
    print("2. No")

    opcion = input("Ingresa una opción: (1/2)")

    if opcion == "1":
        caracteres = string.ascii_letters + string.digits + string.punctuation
        result = "".join(random.choice(caracteres) for _ in range(10))
        print("Tu contraseña aleatoria es: ", result)
    elif opcion == "2":
        print("bye")
        break
    else:
        print("Opción no valida, intenta de nuevo")
