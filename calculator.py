from logica import dividir, multiplicar, restar, sumar

while True:
    
     operacion= input("\n¿Qué operación desea realizar? Introduzca '+' para suma; '-' para resta, '*' para multiplicación o '/' para división: ").lower() .strip()
     num1= float(input("\nIntroduzca el primer número: "))
     num2= float(input("\nIntroduzca el segundo número: "))
    
     if operacion =="+":
          print(f"\nLa suma es: {sumar(num1, num2)}")
     elif operacion== "-":   
          print(f"\nLa resta es: {restar(num1, num2)}")
     elif operacion == "*":
          print(f"\nLa multiplicación es: {multiplicar(num1, num2)}")
     elif operacion =="/" and num2==0:
          print("\nLa división por cero no está permitida")
     elif operacion== "/" and num2!= 0:
          print(f"\nLa división es: {dividir(num1, num2)}")
     else:
          print("No válido")
     continuar= input("¿Desea hacer otro cálculo (s/n)?: ")
     if continuar != "s":
          print("Hasta luego. ")
     break 