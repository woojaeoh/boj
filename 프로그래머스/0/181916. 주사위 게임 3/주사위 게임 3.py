def solution(a, b, c, d):
    #4개가 다 같은 경우
    if (a==b==c==d):
        return a*1111
    
    #3개가 같고 한개가 다른 경우
    if (a==b==c!=d):
        return (10*a+d)**2
    if (a==b==d!=c):
        return (10*a+c)**2
    if (a==c==d!=b):
        return (10*a+b)**2
    if (b==c==d!=a):
        return (10*b+a)**2
    
    #두개씩 같은 경우
    if (a==b) and (c==d):
        return (a+c)*abs(a-c)
    if (a==c) and (b==d):
        return (a+b)*abs(a-b)
    if (a==d) and (b==c):
        return (a+b)*abs(a-b)
    
    #두개가 같고 나머지 하나 하나 다른 경우
    if a==b or a==c or a==d :
        same=a
        others=[x for x in [b,c,d] if x!=a]
        return others[0]* others[1] 
    
    if b==c or b==d :
        same=b
        others=[x for x in [a,c,d] if x!=b]
        return others[0]* others[1]
    
    if c==d:
        same=c
        others=[x for x in [a,b,d] if x!=c]
        return others[0]*others[1]
    
    
    
    if a!= b!= c!= d:
        return min(a,b,c,d)
    
    
    
    
    
    
  