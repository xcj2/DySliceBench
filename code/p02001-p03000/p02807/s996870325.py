from sys import stdout
printn = lambda x: stdout.write(x)
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
DBG = True  and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

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

# #
n = inn()
x = inl()

modinva = [1]*(n+1)
fact = 1
for i in range(2,n):
    modinva[i] = modinv(i,R)
    fact = (fact*i)%R
ddprint(modinva)
ddprint(fact)

acc = [0]*n
for i in range(n):
    acc[i] = acc[i-1]+x[i]

sm = 0
for i in range(n-2,-1,-1):
    e = (x[n-1]-x[i])*modinva[1+i]
    sm = (sm+e)%R
    #ddprint("i {} e1 {} e2 {} sm {} inv2 {}".format(i,e1,e2,sm,inv2))
print((fact*sm)%R)
