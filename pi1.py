
def pi(ep):
    s=0
    signe=1
    i=1
    while (1/i)>=ep:
        s+=1/i*signe
        i+=2
        signe=-signe
                    
    return(s*4); 
    
 
