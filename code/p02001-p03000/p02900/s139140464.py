import random

a,b = map(int,input().split())

def is_prime(q,k=50):
    q = abs(q)
    #計算するまでもなく判定できるものははじく
    if q == 2: return True
    if q < 2 or q&1 == 0: return False

    #n-1=2^s*dとし（但しaは整数、dは奇数)、dを求める
    d = (q-1)>>1
    while d&1 == 0:
        d >>= 1
    
    #判定をk回繰り返す
    for i in range(k):
        a = random.randint(1,q-1)
        t = d
        y = pow(a,t,q)
        #[0,s-1]の範囲すべてをチェック
        while t != q-1 and y != 1 and y != q-1: 
            y = pow(y,2,q)
            t <<= 1
        if y != q-1 and t&1 == 0:
            return False
    return True

def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct


def num(fct):
    a = 1
    for base, exponent in fct:
        a = a * base**exponent
    return a

def divisorize(fct):
    b, e = fct.pop()  # base, exponent
    pre_div = divisorize(fct) if fct else [[]]
    suf_div = [[(b, k)] for k in range(e + 1)]
    return [pre + suf for pre in pre_div for suf in suf_div]

x=[]
y=[]
z=[]

if a==1:
  x.append(1)
else:
  fct_a = factorize(a)
  for div in divisorize(fct_a):
    x.append(num(div))

if b==1:
  y.append(1)
else:
  fct_b = factorize(b)
  for div in divisorize(fct_b):
    y.append(num(div))

z=x+y
w=[m for m in set(z) if z.count(m) > 1]

c=0

for i in range(0,len(w)):
  if is_prime(w[i]):
    c+=1
print(c+1)