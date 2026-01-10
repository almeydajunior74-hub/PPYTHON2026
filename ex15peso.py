maior = 0
menor = 0
print("""qual é o maior e o menor peso""")
for p in range(1,5):
    n = float(input("\nDigite seu peso : "))
    if p ==1:
        maior = n
        menor = n
    else:
        if n > maior:
           maior = n
        if n < menor:
            menor = n
print(f"e o maior {maior} o menor é {menor}")

