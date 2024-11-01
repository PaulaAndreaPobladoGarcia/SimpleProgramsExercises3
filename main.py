# Paso 1: Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

# Paso 2: Usar un bucle para mostrar la tabla de multiplicar
# El bucle va desde 1 hasta 10
for i in range(1, 11):
    # Paso 3: Calcular el resultado de la multiplicación
    resultado = numero * i
    
    # Paso 4: Mostrar el resultado en pantalla
    print(numero, "x", i, "=", resultado)
