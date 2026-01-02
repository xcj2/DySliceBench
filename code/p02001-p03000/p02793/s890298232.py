n=int(input())
l=list(map(int,input().split()))

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

#factorization(24) 

## [[2, 3], [3, 1]]
z=[0]*(10**6+1)
for i in l:
    if i>=2:
        re=factorization(i)
        for p in re:
            z[p[0]]=max(z[p[0]],p[1])
def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]

# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return (m+x%m)%m
w=1
mod=10**9+7
for i in range(10**6+1):
    w*=pow(i,z[i],mod)
    w%=mod
kai=0
for i in l:
    kai+=w*mod_inv(i,mod)
    kai%=mod
print(kai)
            