n = 1  
fraccion = 0.5  
suma = 0  

print(f"{'Potencia':<10}{'Fracción':<15}{'Suma'}")

while fraccion > 0.000001:
    suma += fraccion  
    print(f"{n:<10}{fraccion:<15}{suma}") 
    n += 1  
    fraccion /= 2  # La siguiente

