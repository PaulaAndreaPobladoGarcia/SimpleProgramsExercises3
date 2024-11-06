num1 = int(input("ingresa el primer numero: "))
num2 = int(input("ingresa el segundo numero: "))

inicio = min(num1, num2)+ 1
fin = max(num1, num2)

suma = 0
for i in range(inicio, fin): 
    suma += i
    print("la suma es", suma)
