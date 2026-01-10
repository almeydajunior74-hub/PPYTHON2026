
peso = float(input("Qual o seu peso em kg:  "))
altura: float = float(input("Qual a sua altura em m: "))

imc = peso / altura**2
print("SEU IMC É DE {:.1f} (e está ".format(imc),end="")

if imc < 18.5:
    print("a baixo do peso)")
elif imc < 25:
    print("no peso ideal)")
elif imc < 30:
    print("em sobrepeso)")
elif imc < 40:
    print("em obesidade)")
elif imc > 40:
    print("em obesidade mórbida)")








