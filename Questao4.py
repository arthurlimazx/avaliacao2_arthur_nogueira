# Lista de Convidados

lista=[]
for v in range(1,7):
    nomecon=str(input(f"Me diga o nome do {v} convidado: "))
    lista.append(nomecon)
tentacon=str(input("Me diga o nome do convidado que você quer verificar: "))

if tentacon in lista:
    print("Seu convidado foi verificado")
else:
    print("Seu convidado não está cadastrado")
