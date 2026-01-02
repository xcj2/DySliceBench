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
def cmb(n, k, mod):
    a=framod(n, mod)
    b=framod(k, mod)
    c=framod(n-k, mod)
    return (a * power(b, mod-2, mod) * power(c, mod-2, mod)) % mod
def main():
    x,y=sorted(map(int,input().split()))
    if (x+y)%3!=0:
        print(0)
        return
    if y>2*x:
        print(0)
        return
    m=(x+y)//3
    a,b=x-m,y-m
    print(cmb(a+b, a,10**9+7))
    
main()