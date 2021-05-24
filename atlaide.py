from random import randint 
p=[]
for i in range(1): 
    p.append(randint(0, 100)) 
print("Jūsu atlaide",p, "%")
def atlaide(c,s,p):
   return c/s*p
c = int(input("Ievadiet dzēriena cenu, eiro - "))
s = 100
p = int(input("Ievadiet Jūsu atlaidi, % - "))
a = atlaide(c,s,p)
print("Jūsu atlaide - ",a, "eiro")
b = print("Jums jāsamaksā",c-a, "eiro")