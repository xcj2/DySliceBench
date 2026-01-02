n=int(input())
a=list(map(int,input().split()))
MOD=10**9+7
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
def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
from collections import defaultdict
d=defaultdict(int)
for i in a:
    s=factorization(i)
    for x,y in s:
        if d[x]<y:
            d[x]=y
lcm=1
for val in d:
    #print(d[val],val,d[val]*val)
    lcm=lcm*pow(val,d[val],MOD)
    lcm%=MOD
#print(lcm)
#print(d)
count=0
for val in a:
    y=modinv(val,MOD)
    x=lcm*y
    #print((y*val)%MOD)
    x%=MOD
    #print(x,count)
    count+=x
    count%=MOD
print(count)
