#calculadora
while True:
    
 operacion= input("¿Qué operación desea realizar? Introduzca '+' para suma; '-' para resta, '*' para multiplicación o '/' para división: ").lower() .strip()
 num1= float(input("Introduzca el primer número: "))
 num2= float(input("Introduzca el segundo número: "))

 s= num1+num2
 r= num1-num2
 m= num1*num2


 if operacion =="+":
    print(f"La suma de los dos números es: {s}")
 elif operacion== "-":
      print(f"La resta de los dos números es: {r}")
 elif operacion == "*":
      print(f"La multiplicación de los dos números es: {m}")
 elif operacion =="/" and num2==0:
      print(f"La división por cero no está permitida")
 elif operacion== "/" and num2!= 0:
      d= num1/num2
      print(f"La división de los dos números es: {d}")
 else:
   print("No válido")
 continuar= input("¿Desea hacer otro cálculo (s/n)?: ")
 if continuar != "s":
     print("Hasta luego. ")
     break 