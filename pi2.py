eps=float(input("donner un epsilon"))
s1=0
signe=1
i=1
while eps<1/i:
    s1+=1/i*signe
    i+=2
    signe=-signe
s1=s1*4

print(s1)
