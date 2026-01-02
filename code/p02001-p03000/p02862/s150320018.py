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

if not(-(-x//2) <= y and y <= x*2):
    print(0)
    exit()

flag = True

count = 0
while flag:
    if y*2 == x: # yCc
        print(comb(y, count, 10**9+7))
        exit()
    if y*2 < x: # ない
        print(0)
        exit()
    
    count += 1
    x += 1
    y -= 1


 