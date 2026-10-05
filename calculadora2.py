while True:
    print ("1.Suma")
    print ("2.Resta")
    print ("3.Multiplicacion")
    print ("4.Division")
    print ("5.Salir")
    opcion = input("Ingrese una opcion: ")  
    suma = 1
    resta = 2
    multiplicacion = 3
    division = 4
    salir = 5

    if opcion >"5" or opcion <"1":
        print ("Opcion incorrecta")

    elif opcion == "1":
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        resultado = num1 + num2
        print ("El resultado de la suma es: ", resultado)
    elif opcion == "2":
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        resultado = num1 - num2
        print ("El resultado de la resta es: ", resultado)
    elif opcion == "3":
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        resultado = num1 * num2
        print ("El resultado de la multiplicacion es: ", resultado)
    elif opcion == "4":
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        if num2 == 0:
            print ("No se puede dividir entre cero")
        else:
            resultado = num1 / num2
            print ("El resultado de la division es: ", round(resultado, 2))
    elif opcion == "5":
        print ("Gracias por usar la calculadora")
        break
