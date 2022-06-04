name="list de nom.txt"

def affiche_file(f_name):
    f=open(f_name,'r')
    x=f.readline()
    while x!="":
        print(x,end='')
        x=f.readline()
    f.close

affiche_file(name)    
    
