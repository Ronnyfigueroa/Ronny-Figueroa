
import random

# Lista de opciones disponibles
opciones = ["piedra", "papel", "tijera"]

print("PIEDRA, PAPEL O TIJERA")

# Entrada de datos del jugador
jugador = input("Elige piedra, papel o tijera: ").lower()

# Generar elección aleatoria de la computadora
computadora = random.choice(opciones)

print("La computadora eligió:", computadora)

# Comparación de resultados
if jugador == computadora:
    print("Empate")

elif (jugador == "piedra" and computadora == "tijera") or \
     (jugador == "papel" and computadora == "piedra") or \
     (jugador == "tijera" and computadora == "papel"):
    print("Ganó")