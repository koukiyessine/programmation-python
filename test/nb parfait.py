name="tesy.txt"
f=open(name,"r")
t=f.readline()

while t!="":
    print(t)
    t=f.readline()
f.close()    
