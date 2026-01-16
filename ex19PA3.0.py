print("   Gerador de PA" )
print("-="*10)
p=int(input("   Primeiro Termo: "))
r=int(input("   Razão: ")) 
cont=0
print(p,end=" - > ")

while cont<=8:    
    print(p+r, end=" - > ")
    cont=cont+1
    p=p+r
print("END! ")

