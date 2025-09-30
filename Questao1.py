# Convidados  que começam com a letra A 


contnao=0
cont=0
lista=[]
for v in range(1,6):
    nome=str(input(f"Me de o {v} nome que você quer cadastrar: "))
    lista.append(nome)
print(lista)
for nome in lista:
    if nome[0]=="a" or nome[0]=="A":
        cont+=1
    else:
        contnao+=1
print(f"As palavra que não começam com a letra A são {contnao}")