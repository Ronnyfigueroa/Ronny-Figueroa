
import random

opciones = ["piedra", "papel", "tijera"]

print("PIEDRA, PAPEL O TIJERA")

# Bucle para validar la entrada
while True:
    jugador = input("Elige piedra, papel o tijera: ").lower()

    if jugador in opciones:
        break  # sale del bucle si es válido
    else:
        print("❌ Opción inválida, intenta otra vez.")

# Elección de la computadora
computadora = random.choice(opciones)
print("La computadora eligió:", computadora)

# Comparación
if jugador == computadora:
    print("Empate")

elif (jugador == "piedra" and computadora == "tijera") or \
     (jugador == "papel" and computadora == "piedra") or \
     (jugador == "tijera" and computadora == "papel"):
    print("Ganó")

else:
    print("Perdió")