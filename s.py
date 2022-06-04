from math import*
a,b,c=int(input("donner un entier a")),int(input("donner un entier b")),int(input("donner un entier c"))
d=pow(b,2)-4*a*c
if d>0:
    print("la solution 1 est:",(-b-sqrt(d))/2*a,"est la solution 2 est:","la solution 1 est:",(-b+sqrt(d))/2*a)
elif d==0:
    print("un seul solution :",-b/2*a)
elif d<0:
    print("impossible est ni pas de solution") 
    
