n1=(int(input("digite um valor: ")),int(input("digite mais um valor: ")),int(input("digite outro valor: ")),int(input("digite o ultimo valor: ")))
cont=n1.count(9)
vez=" "
if cont>=2:
    vez="vezes"
else:
    vez="vez"
for n in n1:
    if n%2==0:
        print(n, end=" ")
print(f"Voce digitou os valores {n1}")
print(f"O valor 9 apareceu {n1.count(9)}ª {vez} ")
print(f"o numero 3 apareceu na posição {n1.index(3)+1}")

