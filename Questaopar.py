# Soma par 

lista=[]
numeropar=0
numeroimpar=0
for x in range(1,11):
    numero=int(input(f"Me de o {x} número: "))
    lista.append(numero)
for numero in lista:
    if x%2==0:
        numeropar+=numero
    else:
        numeroimpar+=numero

print(f"a soma do total de números pares foi {numeropar}")    
print(f"a soma do total de números impares foi {numeroimpar}")    
