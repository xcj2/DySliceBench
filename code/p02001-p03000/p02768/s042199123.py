mod = 1000000007

def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y//2)**2 % mod
    else            : return power(x, y//2)**2 * x % mod

def cmb(a,b):
    r=min(b,a-b)
    if(r==0):
        return 1
    ue=1
    sita=1
    for i in range(r):
        ue*=a-i
        ue%=mod
        sita*=r-i
        sita%=mod
    return div(ue,sita)

def div(a, b):
    return mul(a, power(b, mod-2))


n,a,b=map(int,input().split())

zen=power(2,n)-1

dame=cmb(n,a)
kirai=cmb(n,b)

ans=(mod*2+zen-dame-kirai) % mod
print(ans)