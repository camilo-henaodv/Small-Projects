while True:
 print ("Bienvenido al calculador de IMC")
 edad = float(input("ingrese su edad"))
 if edad <12 or edad >67:
    print ("Usted no puede ingresar")
    continue

 nombre = input("Ingrese su nombre")
 peso = float(input("Ingrese su peso"))
 altura = float(input("Ingrese su altura en metros"))

 IMC = peso / (altura ** 2)

 if edad <12 or edad >67:
    print ("Usted no puede ingresar")

 elif edad >=12 and edad <=67:
    print ("""Puede ingresar
    Bienvenido""", nombre)
    print (nombre, "Su IMC es", (round(IMC, 2)))
    if IMC < 18.5:
        print("Usted tiene bajo peso")
    elif IMC < 25: print ("Usted tiene un peso normal")
    elif IMC < 30: print ("Usted tiene sobrepeso")
    else: print ("Usted tiene obesidad")



