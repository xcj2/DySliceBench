def witness(a,n,t,u):
    x=pow(a,u,n)
    for _ in range(t):
        y=(x*x)%n
        if y==1 and x!=1 and x!=(n-1):
            return True
        x=y
    return y!=1

def is_probably_prime(n,witnesses):
    t=1
    u=n>>1
    while u&1==0:
        t+=1
        u>>=1
    assert(2**t*u==n-1)
    for a in witnesses:
        if a<n and witness(a,n,t,u):
            return False
    return True

def is_definitely_prime(n):
    if ((not (n&1)) and n!=2) or (n<2) or ((n%3==0) and (n!=3)):
        return False
    elif n<=3:
        return True
    else:
        return is_probably_prime(n,[2,7,61])

n=10**5
P=[0]*(n+1)
for i in range(n):
    if is_definitely_prime(i+1) and is_definitely_prime((i+2)//2):
        P[i+1]=P[i]+1
    else:
        P[i+1]=P[i]
q=int(input())
Q=[tuple(map(int,input().split())) for _ in range(q)]
for l,r in Q:
    ans=P[r]-P[l-1]
    print(ans)