from math import*
def suite(r):
    a=4
    b=2
    c=1
    for i in range (1,r-2):
        x=sqrt(2*a+c)+b
        a,b,c=b,c,x
    return x
