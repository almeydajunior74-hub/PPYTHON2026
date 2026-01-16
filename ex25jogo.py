from random import randint
print("~"*25)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("~"*25)
#escolha do pc
computador=randint(0,10)

while True:
    #escolha do jogador
    n= int(input("digite um valor "))
    i=str(input("Par OU Impar[P/I] ")).strip()[0].upper
    #soma pra saber se é impar ou par 
    soma=computador+n

    if soma%2==0:
        r=("PAR").strip()[0]
    else:
        r=("IMPAR").strip()[0]
            


    print("VAMOS JOGAR NOVAMENTE")
    print(f"voce jogou {n} e computador {computador}. Total de {n+computador} DEU {r}")




