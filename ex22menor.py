cont=soma=maior=menor=0
resp="b"
while resp!="N":
    n=int(input("Digite um numero "))
    cont+=1
    soma=(soma+n)
    if cont==1:
        maior=n=menor
    else:
        if n > maior:
             maior= n
        if n< menor:
            menor=n
    resp=str(input("Quer continuar ? [S/N] ")).upper().strip()[0]
print(f"(voce digitou {cont} numeros e {soma/cont} é a media)")
print(f"o maior valor foi {maior} e o menor foi {menor}")
