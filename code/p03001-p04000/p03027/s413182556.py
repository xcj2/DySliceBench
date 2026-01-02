printn = lambda x: sys.stdout.write(x)
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
DBG = True  and False
def ddprint(x):
  if DBG:
    print(x)

# extended gcd and modinv
# x = y*(x/y) + x%y
#   ->  g = ax+by = a(y*(x/y) + x%y) + by
#         = (a*(x/y) + b)*y + a*(x%y)
#
# while  g=ax+by, b==0  ->  g=x, a=1

def exgcd(x,y):
    if y == 0:
        return (x,1,0)
    else:
        g,b,a = exgcd(y, x%y)
        return (g, a, b-(x//y)*a)

# return y s.t. x*y mod p == 1
def modinv(x,p):
    return pow(x,p-2,p)


def modinv2(x,p):
    g,a,b = exgcd(x,p)  # ax+bp = g, g=1 if mutually prime
    return a%p


R = 1000003
facts = [1] * R
for i in range(2,R):
    facts[i] = (facts[i-1]*i)%R

qq = inn()
for q in range(qq):
    x,d,n = inm()
    if d==0:
        print(pow(x,n,R))
        continue
    xd = modinv(d,R)
    y = (x * xd) % R
    if y+n-1 >= R:
        print(0)
    else:
        z = pow(d,n,R) * facts[y+n-1] * modinv(facts[y-1],R)
        print(z%R)
