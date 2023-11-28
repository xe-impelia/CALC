while True:
  opcion = int(input("Introduce opción: "))
  if opcion == 0:
    break
  if opcion == 1:
    val1 = int(input("Introduce primer valor: "))
    val2 = int(input("Introduce segundo valor: "))

    suma = val1 + val2
    print(suma)
  elif opcion == 2:
    val1 = int(input("Introduce primer valor: "))
    val2 = int(input("Introduce segundo valor: "))
    resta = val1 - val2
    print(resta)

  elif opcion == 3:
    valor1 = int(input("Introduce primer valor: "))
    valor2 = int(input("Introduce segundo valor: "))
    divi = valor1 / valor2
    print(divi)
    
  if opcion == 4:
      val1 = int(input("Introduce primer valor: "))
      val2 = int(input("Introduce segundo valor: "))
      mult = val1 * val2
      print(mult)

print("ASFASF")