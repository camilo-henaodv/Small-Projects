while True:
 print ("Gases ideales")
 opcion = int(input("""Ingrese lo que quiere calcular
  la ecuacion base es PV = nRT
1. presion
2. volumen
3. temperatura
4. moles 
5. constante de los gases
6. convertir unidades
7. salir"""))

 

 if opcion >7 and opcion <1: 
   print ("No es valido")
               
 

 
 elif opcion == 1: 
  print ("calculara presion")
  mol = float(input("Ingrese moles"))
  constante = float(input("Ingrese la constante"))
  temp = float(input("Ingrese la temperatura en kelvin"))
  volumen = float(input("Ingrese el volumen en L"))
  presion = (mol * constante * temp) / volumen

  print ("La presion es de", round (presion, 2), "atm")

         








 elif opcion == 2: 
   print ("calculara volumen")
   mol1= float(input("Ingrese moles"))
   constante1 = float(input("Ingrese constante"))
   temp1 = float(input("Ingrese temperatura en kelvin"))
   presion1 = float(input("Ingrese presion en atm"))
   volumen1 = (mol1 * constante1 * temp1) / presion1
   print ("El volumen es de", round(volumen1, 2), "L")
          





 elif opcion == 3:
   print ("calculara temperatura")
   mol2 = float(input("Ingrese moles"))
   constante2 = float(input("Ingrese la constante"))
   presion2 = float(input("Ingrese la presion en atm"))
   volumen2 = float(input("Ingrese el volumen en L"))
   temp2 = (presion2 * volumen2) / (mol2 * constante2)
   print ("La temperatura es de", round(temp2,2), "K")







 elif opcion == 4:
   print ("calculara moles")
   constante3 = float(input("Ingrese la constante"))
   presion3 = float(input("Ingrese la presion en atm"))
   volumen3 = float(input("Ingrese el volumen en L"))
   temp3 = float(input("Ingrese la temperatura en kelvin"))
   mol3 = (presion3 * volumen3) / (constante3 * temp3)
   print ("Los moles son", round(mol3, 2))







 elif opcion == 5:
   print ("Calculara la constante de los gases")
   presion4 = float(input("Ingrese la presion en atm"))
   volumen4 = float(input("Ingrese el volumen en L"))
   temp4 = float(input("Ingrese la temperatura en kelvin"))
   mol4 = float(input("Ingrese mol"))
   constante4 = (presion4 * volumen4) / (mol4 * temp4)
   print ("La constante es de", round(constante4, 2))




 elif opcion == 6:
   print ("""Conversion de unidades
   1. Presion
   2. Temperatura
   3. Volumen""")
   eleccion = input("Que desea convertir?")
   if eleccion == "1":
     unidadp = input("""Que unidades desea convertir?
     1.Pascal a atm
     2.mmHg a atm
     3.torr a atm""") 
     if unidadp == "1":
       cantidadpascal = float(input("Ingrese la cantidad de pascales que tiene"))
       resultadopascalatm = cantidadpascal / 101300
       print ("Usted tiene", resultadopascalatm, "atm")
     elif unidadp == "2":
       cantidadmmHg = float(input("Ingrese la cantidad de mmHg que tiene"))
       resultadommHgatm = cantidadmmHg / 760
       print ("Usted tiene", resultadommHgatm, "atm")
     elif unidadp == "3":
       cantidadtorr = float(input("Ingrese la cantidad de torr que tiene"))
       resultadotorratm = cantidadtorr / 760
       print ("Usted tiene", resultadotorratm, "atm")
   elif eleccion == "2":
     unidadT = input("""Que unidades desea convertir?
     1.°C a K
     2.°F a K
     3.°R a K""")
     if unidadT == "1":
       cantidadC = float(input("Ingrese la cantidad de celsius"))
       resultadoCK = cantidadC + 273.15
       print ("Usted tiene", resultadoCK, "K")
     elif unidadT == "2":
       cantidadF = float(input("Ingrese la cantidad de fahrenheit"))
       resultadoFK = ((cantidadF - 32) * 5/9) + 273.15
       print ("Usted tiene", resultadoFK, "K")
     elif unidadT == "3":
       cantidadR = float(input("Ingrese la cantidad de rankine"))
       resultadoRK = cantidadR * 5/9
       print ("Usted tiene", resultadoRK, "K")
   elif eleccion == "3":
     unidadV = input("""Que unidades desea convertir?
     1. Cm^3 a L
     2. m^3 a L
     3. mL a L
     4. Oz a L
     5. Gal a L""")
     if unidadV == "1":
       cantidadcm3 = float(input("Ingrese la cantidad de cm^3"))
       resultadocmL = cantidadcm3 / 1000
       print ("Usted tiene", resultadocmL, "L")
     elif unidadV == "2":
       cantidadm3 = float(input("Ingrese la cantidad de m^3"))
       resultadom3L = cantidadm3 * 1000
       print ("Usted tiene", resultadom3L, "L")
     elif unidadV == "3":
       cantidadmL = float(input("Ingrese la cantidad de mL"))
       resultadoml = cantidadmL / 1000
       print ("Usted tiene", resultadoml, "L")
     elif unidadV == "4":
       cantidadOzl = float(input("Ingrese la cantidad de Oz"))
       resultadoOzl = cantidadOzl / 33.814
       print ("Usted tiene", resultadoOzl, "L")
     elif unidadV == "5":
       cantidadgal = float(input("Ingrese la cantidad de Gal"))
       resultadogal = cantidadgal * 3.785
       print ("Usted tiene aproximadamente", resultadogal, "L")
 elif opcion == 7:
   print ("Gracias por utilizar")
   break

     

                         

                




