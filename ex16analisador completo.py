while True:
    sex=str(input("informe seu sexo[M\F] ")).upper()[0].strip()
    if sex == "M":
        print("sexo Masculino resgistrado com sucesso ")
    elif sex == "F":
        print("sexo Feminino resgistrado com sucesso ")
    elif sex != "M" and sex != "F":
        sex=str(input("\033[032mDados invalidos.Por favor, infrome o sexo: ")).upper()[0].strip()

        