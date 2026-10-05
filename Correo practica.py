opcion = input("Calculadora notas por area, ingrese la materia que preocupa: matematicas, ciencias naturales, humanidades")
if opcion == "ciencias naturales":
 r1 = float(input("Ingrese biologia primer periodo"))
 r2 = float(input("Ingrese quimica primer periodo"))
 r3 = float(input("Ingrese fisica primer periodo"))
 fisica = r3 * 0.40
 quimica = r2 * 0.40
 biologia = r1 * 0.20
 promedio_1 = round((fisica + quimica + biologia) * 0.30, 2)

 r11 = float(input("Ingrese biologia segundo periodo"))
 r22 = float(input("Ingrese quimica segundo periodo"))
 r33 = float(input("Ingrese fisica segundo periodo"))
 fisica1 = r33 * 0.40
 quimica1 = r22 * 0.40
 biologia1 = r11 * 0.20
 promedio_2 = round((fisica1 + quimica1 + biologia1) * 0.30, 2)

 r111 = float(input("Ingrese posible biologia tercer periodo"))
 r222 = float(input("Ingrese posible quimica tercer periodo"))
 r333 = float(input("Ingrese posible fisica tercer periodo"))
 fisica2 = r333 * 0.40
 quimica2 = r222 * 0.40
 biologia2 = r111 * 0.20
 promedio_3 = round((fisica2 + quimica2 + biologia2) * 0.40, 2)

 resultadofinal = round(promedio_1 + promedio_2 + promedio_3, 2)

 print ("Su nota final es", resultadofinal)

 if resultadofinal >=3.5: print ("No viene a nivelacion")
 else: print ("Tiene que venir a nivelar")
elif opcion == "matematicas":
 rr1 = float(input("Ingrese matematicas primer periodo"))
 rr2 = float(input("Ingrese matematicas segundo periodo"))
 rr3 = float(input("Ingrese posible matematicas tercer periodo"))
 rr11 = rr1 * 0.30
 rr22 = rr2 * 0.30
 rr33 = rr3 * 0.40
 resultadomat = round(rr11 + rr22 + rr33, 2)
 print ("Su nota final es", resultadomat)
 if resultadomat >=3.5:
  print ("No viene a nivelar")
 else: print ("Viene a nivelar")
elif opcion == "humanidades":
 rh1 = float(input("ingrese la nota de Ingles primer periodo"))
 rhe1 = float(input("ingrese la nota de español primer periodo"))
 ingles1 = rh1 * 0.50
 español1 = rhe1 * 0.50
 hum1 = round((ingles1 + español1) * 0.30, 2)
 rh2 = float(input("ingrese la nota de Ingles segundo periodo"))
 rhe2 = float(input("ingrese la nota de español segundo periodo"))
 ingles2 = rh2 * 0.50
 español2 = rhe2 * 0.50
 hum2 = round((ingles2 + español2) * 0.30, 2)
 rh3 = float(input("Ingrese la posible nota ingles tercer periodo"))
 rhe3 = float(input("Ingrese la posible nota español tercer periodo"))
 ingles3 = rh3 * 0.50
 español3 = rhe3 * 0.50
 hum3 = round((ingles3 + español3) * 0.40, 2)
 resultadohum = round(hum1 + hum2 + hum3, 2)
 print ("Su nota final es",resultadohum)
 if resultadohum >=3.5:
  print ("No tiene que venir a nivelar")
 else: print ("Tiene que nivelar")
       










