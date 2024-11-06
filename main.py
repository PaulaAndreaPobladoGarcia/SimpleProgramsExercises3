altura = int(input("ingrese cuanto quiere que sea de alto: "))
ancho = int(input("ingrese cuanto quiere que se de ancho: "))

for i in range(altura):
    print("*" * ancho)

altura = int(input("Altura: "))


for i in range(1, altura + 1):  
    print("*" * i)  


lado = int(input("Lado: "))

for i in range(lado):
    print(" " * (lado - i - 1) + "*" * (2 * i + 2))  

for i in range(lado - 1):
    print(" " * (i + 1) + "*" * (2 * (lado - i - 2) + 2)) 