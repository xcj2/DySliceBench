def find_power(n,mod):
    # 0!からn!までのびっくりを出してくれる関数(ただし、modで割った値に対してである）
    powlist=[0]*(n+1)
    powlist[0]=1
    powlist[1]=1
    for i in range(2,n+1):
        powlist[i]=powlist[i-1]*i%(mod)
    return powlist

def find_inv_power(n):
    #0!からn!までの逆元を素数10**9+7で割ったあまりリストを作る関数
    powlist=find_power(n,10**9+7)
    check=powlist[-1]
    first=1
    uselist=[0]*(n+1)
    secondlist=[0]*30
    secondlist[0]=check
    secondlist[1]=check**2
    for i in range(28):
        secondlist[i+2]=(secondlist[i+1]**2)%(10**9+7)
    a=format(10**9+5,"b")
    for j in range(30):
        if a[29-j]=="1":
            first=(first*secondlist[j])%(10**9+7)
    uselist[n]=first
    for i in range(n,0,-1):
        uselist[i-1]=(uselist[i]*i)%(10**9+7)
    return uselist

def combi(a,b,n,r,mod):
    if n<r:
        return 0
    elif n>=r:
        return (a[n]*b[r]*b[n-r])%(mod)
aa=find_power(10**5,10**9+7)
bb=find_inv_power(10**5)
mod=10**9+7

n,k=map(int,input().split())
lists=list(map(int,input().split()))
import collections 
L=collections.Counter(lists)
L=dict(L)
uselist=[]
for a,v in L.items():
    uselist.append((a,v))
uselist=sorted(uselist,key=lambda x:x[0])
maxlist=[(0,0)]

counter=0
for some in uselist:
    counter+=some[1]
    maxlist.append((some[0],counter))

MAX=0

for j in range(1,len(maxlist)):
    MAX+=(combi(aa,bb,maxlist[j][1],k,mod)-combi(aa,bb,maxlist[j-1][1],k,mod))*maxlist[j][0]
    MAX=MAX%mod

  
uselist=uselist[::-1]

maxlist=[(0,0)]

counter=0
for some in uselist:
    counter+=some[1]
    maxlist.append((some[0],counter))

MIN=0

for j in range(1,len(maxlist)):
    MIN+=(combi(aa,bb,maxlist[j][1],k,mod)-combi(aa,bb,maxlist[j-1][1],k,mod))*maxlist[j][0]
    MIN=MIN%mod

print((MAX-MIN)%mod)
