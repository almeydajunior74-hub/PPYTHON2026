# m=0
# f=0
# maior=0
# while True:
#     print("-"*20)
#     print("CADASTRE UMA PESSOA")
#     print("-"*20)
#     idade=int(input("Idade: "))
#     sexo=str(input("Sexo: [M/F]")).strip()[0].upper()
#     print("-"*20)
#     quer=str(input("Quer continuar? [S/N]")).upper().strip()[0]

#     if idade > 18:
#         maior+=1
#     if sexo not in "mM":
#         h+=1
#     if idade<20:
#             m+=1
#     if quer not in"sS":
#         break
# print(f"Total de pessoas com mais de 18 anos: {idade}")
# print(f"Ao todo temos {h} homens cadastrados")
# print(f"e temos {m} mulheres com menos de 20 anos")





while True:
    idade=int(input("Idade: "))
    sexo=" "
    while sexo not in "MF":
        sexo=str(input("Sexo: [M/F]")).strip().upper()[0]

    resp=" "
    while resp not in "SN" :
        resp=str(input("quer continuar")).strip().upper()[0]
    if resp=="N":
        break
print("acabou")


