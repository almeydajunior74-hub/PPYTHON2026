print("Gerador de PA")  
print("-="*10)
n = int(input("primeiro termo:  "))
r = int(input("razão: "))
cont=0
g=10
while cont<=g:
    print(n+r,end=" -> ")
    cont=cont+1
    n=n+r
print("END")
 