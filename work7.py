n=int(input("donner un valeur de n "))
m=int(input("donner un valeur de m "))

s1,s2=0,0
for i in range(2,(n//2)+1):
    if i%2==0:
        s1+=i
                
for j in range(2,(m//2)+1):
    if j%2==0:
        s2+=j
        
if s1==m and s2==n:
    print("le nombre ",n,"est",m,"sont amis")
else:
      print("le nombre ",n,"est",m,"ni sont pas amis")
    
    
