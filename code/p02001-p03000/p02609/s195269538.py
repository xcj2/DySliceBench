def mpow(a,b,m):
    ans=1
    while b >0 :
        if b&1:
            ans = (ans*a)%m
        a=(a*a)%m
        b=b>>1

    return ans

def calcmod(X,m,N):
    mod=0
    X=X[::-1]
    # print(X)
    for i in range(N):
        if X[i] == '1':
        # if X & (1<<i) >0:
            mod += mpow(2,i,m)
            mod%=m
    return mod

def popcount(m):
    return bin(m).count("1")


def findsteps(mm):
    cnt=0
    while mm !=0:
        cnt+=1
        mm=mm%popcount(mm)
    return cnt
N=int(input())
x=input()
X=int(x,2)

##we need to find X%(m-1) and X%(m+1)
m=popcount(X)
m1=m+1
m2=m-1
firstmod=calcmod(x,m1,N)
if m2 !=0:
    secondmod=calcmod(x,m2,N)
fans=[0 for i in range(N)]
k=0
for i in range(N-1,-1,-1):
    if X & (1<<i) >0:
        ##the bit was set
        ##we need to find X%(m-1) - (2^i)%(m-1)
        if m2 == 0:
            ans=0
        else:
            mm=secondmod - mpow(2,i,m2)
            if mm < 0:
                mm+=m2
            mm=mm%m2
            ans=1+findsteps(mm)
    else:
        mm = firstmod + mpow(2,i,m1)
        mm=mm%m1
        ans=1+findsteps(mm)
    fans[k] = ans
    k+=1
        ##the bit was not set
for i in fans:
    print(i)