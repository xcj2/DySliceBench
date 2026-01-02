from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True  and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

def modinv2(x,r):
  return pow(x,r-2,r)

def comb(n,a):
    dend = n
    for i in range(1,a):
        dend = (dend*(n-i))%R
    sor = 1
    for i in range(2,a+1):
        sor = (sor*i)%R
    return (dend*modinv2(sor,R))%R

n,k = inm()
if n-1<=k:
    print(comb(2*n-1,n-1))
    exit()
c = [1]*(k+1)
d = [1]*(k+1)
for i in range(1,k+1):
    m = modinv2(i,R)
    c[i] = (c[i-1]*(n-i+1)*m)%R
    d[i] = (d[i-1]*(n-i)*m)%R
ddprint("c,d")
ddprint(c)
ddprint(d)
sm = 0
#for j in range(n-k,n+1):
#    sm = (sm+comb(n,j)*comb(n-1,j-1))%R
for j in range(k+1):
    sm = (sm+c[j]*d[j])%R
if k==1:
    sm = (sm-1)%R
print(sm)
