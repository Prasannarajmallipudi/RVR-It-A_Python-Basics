def value(s):
    k=len(s)
    l,d,u,dp=0,0,0,0
    w=len(s.split())
    for i in range(0,k):
        if(s[i].isalpha()):
            if(s[i].islower()):
                l=l+1
            elif(s[i].isupper()):
                u=u+1
        elif(s[i].isdigit()):
            d=d+1
                
                
            
        else:
            dp=dp+1
            
    print("lower",l,"upper",u,"digit",d,"special",dp,"words",w)
s=input("enter string")
value(s)
        
    
