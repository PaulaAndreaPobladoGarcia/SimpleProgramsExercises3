def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def estimar_e():
    n = 10  
    suma = 0
    anterior = 0
    while True:
        
        actual = factorial(n)
        
        
        suma += actual
        
        if abs(actual - anterior) < 0.0001:
            break
        
        anterior = actual
        
        n += 1
    
    return suma

e_aproximado = estimar_e()
print(f"Valor aproximado de e: {e_aproximado}")
