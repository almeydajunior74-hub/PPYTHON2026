from random import randint
f=randint(0,10)
soma=0
print("TENTE ADIVINHA QUE NUMERO ESTOU PENSANDO ENTRE 0 E 10")
while True:
    n=int(input("qual seu palpite? "))
    soma+=1
    if n>f:
        print("MENOS")
    elif n<f:
        print("MAIS")
    elif n==f:
        print("ACERTOU COM {} TENTATIVAS".format(soma))


