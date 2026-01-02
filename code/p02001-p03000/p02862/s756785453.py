import sys
input = sys.stdin.readline


MOD=10**9+7
def mod(a):
    return a%MOD

x,y=map(int,input().split())

if((x+y)%3!=0):
    print(0)  
    exit()
n=(x+y)/3
x-=n
y-=n
if x<0 or y<0:
    print(0) 
    exit()

def po(a,b):
    if(b==0):return 1
    if(b==1):return mod(a)
    if(b%2==0):return mod(po(mod(a*a),b/2))
    return mod(po(a,b-1)*a)
    
def bunbo(a):
    return po(a,MOD-2)
    
def comb(a,b):
    res=kai[a]
    res=mod(res*bunbo(kai[b]))
    res=mod(res*bunbo(kai[a-b]))
    return res
    
N=(10**6)*2+5
#N=100
kai=[0]*N

kai[0]=1
for i in range(1,N-1):
    kai[i]=mod(kai[i-1]*i)

#print(kai)
print(comb(int(x+y),int(x)))
"""
for i in range(8):
    for j in range(i):
        print(comb(i,j),end=" ")
    print()
"""