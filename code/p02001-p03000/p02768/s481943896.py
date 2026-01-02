mod=10**9+7

def add(a, b):
    return (a + b) % mod

def sub(a, b):
    return (a + mod - b) % mod

def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
#    else            : return power(x, y-1)* x % mod
    
    elif y % 2 == 0 : return power(x, y//2)**2 % mod
    else            : return power(x, y//2)**2 * x % mod

def div(a, b):
    return mul(a, power(b, mod-2))

n,a,b=map(int,input().split())


n2=power(2,n)
#n2=1
#for i in range(n):
#    n2=mul(n2,2)
n2=sub(n2,1)
#print(n2)
    
na=1
pna=1
for i in range(a):
    na=mul(na,(n-i))
    pna=mul(pna,(i+1))    
#print(na,pna)
na=div(na,pna)
       
nb=1
pnb=1
for i in range(b):
    nb=mul(nb,(n-i))
    pnb=mul(pnb,(i+1))    
#print(nb,pnb)
nb=div(nb,pnb)

#print(na,nb)

n2=sub(n2,na)
n2=sub(n2,nb)
print(n2)