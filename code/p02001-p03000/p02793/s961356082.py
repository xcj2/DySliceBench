import math

def Sieve_of_Eratosthenes(N):
    if N<2: return set()
    prime=set(i for i in range(2,N+1))
    for i in range(2,math.ceil(N**0.5)+1):
        tmp=set()
        for j in prime:
            if j>i and j%i==0: tmp.add(j)
        for j in tmp:
            prime.remove(j)

    return prime

def gcd(a,b):
    if b>a:
        a,b=b,a
    while b:
        a,b=b, a%b
    return a

def egcd(a, b):
    (x, lastx) = (0, 1)
    (y, lasty) = (1, 0)
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return (lastx, lasty, a)

# ax ≡ 1 (mod m)なるxを返す
def modinv(a, m):
    (inv, q, gcd_val) = egcd(a, m)
    return inv % m

MOD=10**9+7
prime=Sieve_of_Eratosthenes(10**3+1)
dic={}
for p in prime:
    dic[p]=0

n=int(input())
a=list(map(int,input().split()))

zz=set()
for i in range(n):
    x=a[i]

    tmpdic={}
    for p in prime:
        if x==1: break
        while x%p==0:
            x=x//p
            if p in tmpdic: tmpdic[p]+=1
            else: tmpdic[p]=1

    if x>1:
        if x in prime:
            if p in tmpdic: tmpdic[p]+=1
            else: tmpdic[p]=1
        else: zz.add(x)

    for p in tmpdic:
        dic[p]=max(tmpdic[p],dic[p])

lcm=1
for p in dic:
    for j in range(dic[p]):
        lcm=(lcm*p)%MOD
for p in zz:
    lcm=(lcm*p)%MOD

ans=0
for i in range(n):
    ans+=modinv(a[i],MOD)
    ans%=MOD
print((ans*lcm)%MOD)