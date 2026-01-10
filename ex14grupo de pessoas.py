from datetime import date
dat = date.today().year
cont = 0
cont2 = 0
for c in range(1,8):
    n = int(input(f"em que ano a {c}ª pessoa nasceu? "))
    if dat-n>=18:
        cont += 1
    else:
        cont2 += 1
print("\033[33mtem {} pessoas de maior de idade \nTem {} pessoas de menor de idade".format(cont,cont2))
