c="listdenom.txt"
f=open(c,"r")
x=f.readline()
while x!="":
    print(x,end="")
    x=f.readline()
f.close()    


f=open(c,"r")
x=f.readline()
while x!="":
    y=f.split(':')
    if int(y[2])>=19:
           print(x,end="")
           x=f.readline()        
f.close()  
