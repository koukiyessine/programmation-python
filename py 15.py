from math import*
def suite(n):
    a,b,c=4,2,1
    for i in range(n):
        d=sqrt(2*a+c)+b
        a,b,c=b,c,d
    return d    
