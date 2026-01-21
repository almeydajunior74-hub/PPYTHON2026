print("*"*25)
valor=int(input("  QUAL O VALOR DE SAQUE: "))
total=valor
ced=50
conta_ced=0
while True:
    if  total>=ced:
        total-=ced
        conta_ced+=1
    else:
        print(f" TOTAL DE {conta_ced} CEDULAS DE R$ {ced}")
        if total==ced:
            total=total-ced
            conta_ced+=1
            
        ced=total
        if total==0:
            break


