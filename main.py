num = int(input("ingresa el numero: "))
divisores = []
for i in range(1,num +1):
    if num % i ==0: 
        divisores.append(i)
print (" ".join(map(str,divisores)))      
