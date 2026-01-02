d = 10**9 + 7

x,y = map(int, input().split())

def numerator(n, k, p):
    l = 1;
    for j in range(k+1,n+1):
        l = (l*j)%p;
    return l

def denominator(n, k, p):
    l = 1;
    for j in range(2,n-k+1):
        l = (l*j)%p;
    return l


def power(a, k, p):
    if (k == 0):
        return 1
    r = power((a*a)%p,k>>0x01,p);
    if ((k&0x01) == 0x01): #odd number
        r = (r*a)%p;
    return r


def n_choose_K(n, k, p):
    num = numerator(n,k,p)
    den = denominator(n,k,p)
    return (num*power(den,p-2,p))%p
    

n = -(x-2*y)/3.0
m = -(-2*x+y)/3.0

if n-int(n) != 0 or m-int(m) != 0:
    print(0)
elif n<0 or m<0:
    print(0)
else:
    n = int(n)
    m = int(m)
    ans = n_choose_K(n+m,n,d)
    print(int(ans))
    
