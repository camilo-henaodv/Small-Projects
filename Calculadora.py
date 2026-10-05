from pdb import Restart


print ("Bienvenido, ingrese la opcion que desee")
print ("1. Suma")
print ("2. Resta")
print ("3. Multiplicacion")
print ("4. Division")

opcion = int(input("Ingrese la opcion que desea: "))
if opcion > 4: print ("No es valido, intente denuevo")

elif opcion == 1:
 suma = float(input("Ingrese su primer numero"))
 suma2 = float(input("Ingrese su segundo numero"))
 resultado = suma + suma2
 print ("El resultado es", resultado)

elif opcion == 2:
 resta = float(input("Ingrese su primer numero"))
 resta2 = float(input("Ingrese su segundo numero"))
 resultado2 = resta - resta2
 print ("El resultado es", resultado2)

elif opcion == 3:
 multiplicacion = float(input("Ingrese su primer numero"))
 multiplicacion2 = float(input("Ingrese su segundo numero"))
 resultado3 = multiplicacion * multiplicacion2
 print ("El resultado es", resultado3)

elif opcion == 4:
 division = float(input("Ingrese su primer numero"))
 division2 = float(input("Ingrese su segundo numero"))
 if division2 == 0:
     print ("No se puede dividir entre cero")

 resultado4 = division / division2

else: 
     resultado4 = division / division2
     print ("El resultado es", round (resultado4, 2))


 




 



 
   
   
    



