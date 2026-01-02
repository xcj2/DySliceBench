def egcd(a, b):
    (x, lastx) = (0, 1)
    (y, lasty) = (1, 0)
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return (lastx, lasty, a)

# ax ≡ 1 (mod m)

def modinv(a, m):
    (inv, q, gcd_val) = egcd(a, m)
    #print(inv, q, gcd_val)
    return inv % m

def m(n,r):
    d=1
    e=1
    f=1
    for i in range(r):
        d=(n-i)
        e=(i+1)
        d%=(10**9+7)
        f = f*d*modinv(e,(10**9+7))%(10**9+7)
        
    return(f)

n=[int(i) for i in input().split()]
a=sum(n)
if a%3 != 0:print(0)

else:
    b=int(a/3)
    if b==1:
        print(1)
    else:
        c=n[0]-b
        d=n[1]-b
        if c<0 or d<0: print(0)

        else:
            if c==d:
                c=int(b/2)
            d=m(b,min(c,d))
            print(d%(10**9+7))