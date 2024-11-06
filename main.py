
def estimar_pi(n):
    suma = 0
    for i in range(n):
        
        signo = (-1) ** i
        
        denominador = 2 * i + 1
        suma += signo / denominador

    pi_estimado = 4 * suma
    return pi_estimado

n = int(input("Ingrese el número de términos (n): "))

pi = estimar_pi(n)
print(f"Estimación de pi con {n} términos: {pi}")
