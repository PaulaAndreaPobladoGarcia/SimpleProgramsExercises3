def longitud_collatz(n):
    longitud = 1  
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        longitud += 1
    return longitud

n = int(input("Ingrese un número entero: "))

for i in range(1, n):
    longitud = longitud_collatz(i)
    print(f"{i} {'*' * longitud}")

