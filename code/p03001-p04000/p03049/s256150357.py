def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(input())
def S(): return list(input())
n=I()
ans=0
sb=0
fa=0
sbfa=0
for i in range(n):
    ts=S()
    if ts[0]=="B" and ts[-1]!="A":
        sb+=1
    elif ts[0]!="B" and ts[-1]=="A":
        fa+=1
    elif ts[0]=="B" and ts[-1]=="A":
        sbfa+=1
    for i in range(len(ts)-1):
        if ts[i]=="A" and ts[i+1]=="B":
            ans+=1
    
p=min(fa,sb,sbfa)
ans+=2*p
if p>0:
    ans+=sbfa-p+min(max(0,fa-p),max(0,sb-p))
else:
    if sbfa==0:
        ans+=min(max(0,fa-p),max(0,sb-p))
    elif sb==0:
        if fa>sbfa:
            ans+=sbfa
        else:
            ans+=sbfa-1+min(1,fa)
    elif fa==0:
        if sb>sbfa:
            ans+=sbfa
        else:
            ans+=sbfa-1+min(1,sb)   
print(ans)