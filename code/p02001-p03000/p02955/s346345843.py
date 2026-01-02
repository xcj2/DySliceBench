import sys,math
printn = lambda x: sys.stdout.write(x)
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
DBG = True  and False

def ddprint(x):
  if DBG:
    print(x)

def prime_division(x):
    q = int(math.sqrt(x))
    a = []
    for i in range(2,q+1):
        ex = 0
        while x%i == 0:
            ex += 1
            x //= i
        if ex>0:
            a.append([i,ex])
    if x>q:
        a.append([x,1])
    return a

def divisorlist(z):
    if len(z)==1:
        return [z[0][0]**i for i in range(z[0][1]+1)]
    y = divisorlist(z[1:])
    s = []
    for i in range(z[0][1]+1):
        for j in y:
            s.append((z[0][0]**i)*j)
    return s

n,k = inm()
a = inl()
sm = sum(a)
zz = prime_division(sm)
z = divisorlist(zz)
z.sort(reverse=True)
ddprint(z)
for p in z:
    if p>sm+k:
        continue
    b = [ai%p for ai in a]
    b.sort()
    s = sum(b)
    m = s//p
    t = sum(b[:n-m])
    ddprint("p {} b {} s {} m {} t {}".format(p,b,s,m,t))
    if t<=k:
        print(p)
        exit()
