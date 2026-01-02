import sys
sys.setrecursionlimit(1000000000)
def framod(n, mod, a=1):
    for i in range(1,n+1):
        a=a * i % mod
    return a

def power(n, r, mod):
    if r == 0: return 1
    if r%2 == 0:
        return power(n*n % mod, r//2, mod) % mod
    if r%2 == 1:
        return n * power(n, r-1, mod) % mod
def comb(n, k, mod):
    a=framod(n, mod)
    b=framod(k, mod)
    c=framod(n-k, mod)
    return (a * power(b, mod-2, mod) * power(c, mod-2, mod)) % mod

x,y=map(int,input().split())
y,x=min(x,y),max(x,y)
if x>2*y or (x+y)%3!=0:
    #print(1)
    print(0)
else:
    print(comb((x+y)//3, min(x,y)-(x+y)//3,10**9+7))