# print(" === Vocales y Consonantes ===")

# while True:
#     print("Ingresa una palabra")
#     texto = input("Ingresa una palabra: ").strip()

#     if not texto.isascii() or not texto.isalpha:
#         print("Eso no es una palabra válida, intenta de nuevo")
#         continue

#     texto = texto.lower()

#     vocales = ["a", "e", "i", "o", "u"]
#     numVocales = 0
#     consonantes = 0

#     for letra in texto:
#         if letra.isalpha():
#             if letra in vocales:
#                 numVocales += 1
#             else:
#                 consonantes += 1

#     print(f"Vocales encontradas: {numVocales}")
#     print(f"Consonantes encontradas: {consonantes}")

#   # Pregunta si quiere seguir
#     seguir = input("¿Quieres ingresar otra palabra? (s/n): ").lower()
#     if seguir != "s":
#         print("¡Gracias!")
#         break

print(" === Vocales y Consonantes ===")

while True:
    texto = input("Ingresa una palabra: ").strip()

    # if not texto.isascii() or not texto.isalpha():
    # El de arriba Es para palabras
    if not texto.isascii():
        print("Eso no es una palabra valida, intenta de nuevo")
        continue

    texto = texto.lower()
    vocales = ["a", "e", "i", "o", "u"]

    # Contar vocales y consonantes en una línea cada uno
    numVocales = sum(1 for letra in texto if letra in vocales)
    consonantes = sum(1 for letra in texto if letra.isalpha()
                      and letra not in vocales)

    print(f"Vocales encontradas: {numVocales}")
    print(f"Consonantes encontradas: {consonantes}")

    seguir = input("¿Quieres ingresar otra palabra? (s/n): ").lower()
    if seguir != "s":
        print("Gracias")
        break
