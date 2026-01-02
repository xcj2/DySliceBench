n,m = map(int,input().split())
def div(x,y):
    if x%y!=0:
        return 0
    else:
        return 1+div(int(x/y),y)

p=[]
q=[]

def fact(s):
    if len(p)!=0:
        k=p[-1]
    else:
        k=2
    for i in range(2,max(int(s**0.5) +2,2)):
        a=div(s,i)
        if a==0:
            0
        else:
            p.append(a)
            q.append(i)
            s=int(s/i**a)
    if s!=1:
        p.append(1)
            
fact(m)
def comb(nn,rr):
    rr=min(rr,nn-rr)
    rt=1
    for i in range(rr):
        #rt=rt*(nn-i)/(rr-i)
        rt*=(nn-i)
    for i in range(rr):
        rt//=(rr-i)
    return int(rt)
#print(p,q,m)
mo=10**9 +7
ans=1
if len(p)==0:
    ans=1
else:
    for i in p:
        ans*=comb(i+n-1, i) % mo
print(ans % mo)
