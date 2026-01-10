

print("="*10,end="")
print(" lojas almeyda ",end="")
print("="*10)

preco= float(input("qual o valor do produto? R$ "))
print("""FROMAS DE PAGAMENTOS
[1]A VISTA
[2]A VISTA NO CARTAO
[3]2X NO CARTAO
[4]3X OU MAIS NO CARTAO""")
numero=int(input("QUAL A OPÇÃO DESEJADA? "))

if numero == 1:
    print("\nValor sai o \033[33m{}". format(preco*0.90))
elif numero == 2:
    print("\nValor sai o \033[33m{}". format(preco*0.95))
elif numero == 3:
    print("\nValor sai o \033[33m{}". format(preco))
elif numero == 4:
    n=int(input("QUANTAS PASRCELAS?? "))
    print("em {} parcelas, sai o total de \033[32m{}, pagando a mais \033[31m{}". format(n,(preco*1.20)/n,preco*0.20))

