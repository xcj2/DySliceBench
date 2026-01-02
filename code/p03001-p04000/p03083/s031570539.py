inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
R = 10**9 + 7
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
    g,a,b = exgcd(x,p)  # ax+bp = g, g=1 if mutually prime
    return a%p

def pw(x,e):
    if e==0:
        return 1
    elif e%2==0:
        return (pw(x,e//2)**2)%R
    else:
        return (x * pw(x,e//2)**2)%R

def rmod(i,qb,qw):
    global two2i, itwo2i
    numer = (two2i[i] - qb + qw)
    iden = itwo2i[i+1]
    ddprint("num {} idn {}".format(numer, iden))
    return (numer*iden)%R

b,w = inm()
ddprint("b {} w {}".format(b,w))

inv2 = modinv(2,R)
fact = [1] * (b+w+2)
for i in range(2,b+w+1):
    fact[i] = (i*fact[i-1])%R
ifact = [1] * (b+w+2)
ifact[b+w] = modinv(fact[b+w],R)
for i in range(b+w-1,0,-1):
    ifact[i] = ((i+1)*ifact[i+1])%R
two2i = [1] * (b+w+2)
itwo2i = [1] * (b+w+2)
itwo2i[1] = inv2
for i in range(1,b+w+1):
    x = (2*two2i[i-1])
    two2i[i] = x if x < R else x-R
    itwo2i[i] = (inv2*itwo2i[i-1]) % R
ddprint(fact[0:5])
ddprint(ifact[0:5])

cb = cw = 1
qb = qw = 0
print(500000004)
for i in range(1,b+w):
    qb = 0 if i<b else 1 if i==b else (2*qb+cb) % R
    qw = 0 if i<w else 1 if i==w else (2*qw+cw) % R
    cb = 1 if i<b else (fact[i]*ifact[b-1]*ifact[i-b+1]) % R
    cw = 1 if i<w else (fact[i]*ifact[w-1]*ifact[i-w+1]) % R
    ddprint("i {} cb {} cw {} qb {} qw {}".format(i,cb,cw,qb,qw))
    print(rmod(i,qb,qw))
