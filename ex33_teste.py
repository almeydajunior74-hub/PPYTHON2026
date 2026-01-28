palavra=('arroz','pao','carne','suco')
for p in palavra:
    print(f"dentro da palavra {p} tem vogais", end="")
    for letra in p:
        if letra.lower() in"aeiou":
            if letra.lower()