# Convidados começa 


lista=[]
for v in range(1,6):
    nome=str(input("Me de o {v} nome que você quer cadastrar: "))
    lista.append(nome)
print(lista)
for nome in lista:
    if nome[0]=="a" or nome[0]=="A":
        lista.remove(nome)
print(f"As palavra que não começam com a letra A são {lista}")