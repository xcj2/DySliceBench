from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
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

n,a,b = inm()
print((pow(2,n,R)-comb(n,a)-comb(n,b)-1)%R)
