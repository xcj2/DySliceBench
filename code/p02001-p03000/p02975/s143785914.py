def MI():
    return map(int,input().split())
def I():
    return int(input())
def LI():
    return [int(i) for i in input().split()]
    
n=I()
a=LI()

a.sort()

def check(n,a):
    if n%3!=0:
        if a[-1]==0 and a[0]==0:
            return True
        else:
            return False
    else:
        m=n//3
        c=a[0]
        for i in range(m):
            if a[i]!=c:
                k=0
                return False
        c=a[m]
        for i in range(m):
            if a[m+i]!=c:
                k=0
                return False
                
        c=a[2*m]    
        for i in range(m):
            if a[2*m+i]!=c:
                k=0
                return False
        if a[0]^a[m]==a[m*2]:
            return True
            
if check(n,a):
    k=0
else:
    k=1
ans=['Yes','No']

print(['Yes','No'][k])
