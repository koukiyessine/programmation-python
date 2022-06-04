from math import*
a=int(input("donner un valeur a :"))
b=int(input("donner un valeur b :"))
c=int(input("donner un valeur c :"))

if(a==0):
      if b!=0:
         print("une seule soultion %.2f" %(-c/b))
      elif c!=0:
         print("soultion impossible")
      else:
         print("la soultion est tt R")
else:
    d=b**2-4*a*c
    if d>0:
        x1=(-b-sqrt(d))/(2*a)
        x2=(-b+sqrt(d))/(2*a)
        print(x1, x2)
    elif d==0:
        print("une seule solution%.3f" %(b/2*a))
    else:
        print("solution impossible")
            
    
