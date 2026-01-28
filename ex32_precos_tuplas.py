print("¨"*50)
print(f'{"LISTA DE PREÇOS":^50}')
print("¨"*50)

#tuplas

listagem=("lápis",1.50,"caneta",2.10,"apontador",2.60,"mochila",40.96)

for c in range(0, len(listagem)):
    if c%2==0:
        print(listagem[c], end="-"*20)
    else:
        print(listagem[c])