# Lista de Convidados

lista=[]
for v in range(1,7):
    nomecon=str(input(f"Me diga o nome do {v} convidado: "))
    lista.append(nomecon)
tentacon=str(input("Me diga o nome do convidado que você quer verificar: "))
if nomecon[0]=="a" or nomecon[0]=="A":
    tentacon[0]==nomecon[0]
if tentacon== lista[0] or tentacon== lista[1] or tentacon== lista[2] or tentacon== lista[3] or tentacon== lista[4] or tentacon== lista[5] or tentacon[0]==nomecon[0] or tentacon[0]!=nomecon[0]:
    print("Seu convidado foi verificado")
else:
    print("Seu convidado não está cadastrado")
    
