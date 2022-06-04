import random

name="texte.txt"
hum="tex.txt"
def humainid(name):
    x=open(name, "r")
    n=random.randint(1,11)
    for i in range(n):
        nom=x.readline()

    x.seek(0)
    n=random.randint(1,11)
    for i in range(n):
        prenom=x.readline()
        
    nom=nom.split("\n")[0]
    prenom=prenom.split("\n")[0]
    jj=random.randint(1,28)
    mm=random.randint(1,12)
    aa=random.randint(1980,2010)

    ch=["@gmail.com", "@hotmail.com", "@yahoo.com"]
    n=random.randint(0,2)
    gmail=nom+prenom+ch[n]
    x.close()

    return nom,prenom,jj,mm,aa,gmail


humainid(name)
