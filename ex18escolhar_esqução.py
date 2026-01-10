n1=int(input("Primeiro valor: "))
n2=int(input("Segundo valor: "))
while True:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do prgrama''')
    Opcao=int(input("qual a opção >> "))
    if Opcao == 1:
        print(f"total é {n1+n2} ")
    elif Opcao == 2:
        print(f"total é {n1*n2} ")
    elif Opcao == 3:
        if n1 > n2:
            print(f"{n1}maior ")
        else:
            print(f"{n2}maior ")
    elif Opcao == 4:
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    else:
        print("ate a proxima, VOLTE SEMPRE")
        break

