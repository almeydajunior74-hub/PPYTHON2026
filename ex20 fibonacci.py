print("="*25)
print("  sequencia de fibonecci")
print("="*25)
t=int(input("Quantos termos vc quer mostrar "))
x=3
t1=0
t2=1
print(f"{t1}->{t2}->",end="")
while x<=t:
    x=x+1
    t3=t1+t2
    print(f"{t3}->", end="")
    t1=t2
    t2=t3
  
print("fim")
     

     