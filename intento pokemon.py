import random
jugador = input("Piedra, papel, o tijera")
opciones = ["piedra", "papel", "tijera"]
cpu = random(opciones)
if cpu == "piedra" and jugador == "papel" or cpu == "papel" and jugador == "tijera" or cpu == "tijera" and jugador == "piedra":
    print ("cpu eligio", cpu, ",ganaste")
else: print ("perdiste")


