def s_in():
    return input()

def n_in():
    return int(input())

def l_in():
    return list(map(int, input().split()))

class Interval():
    def __init__(self, li):
        self.li = li
        self.n = len(li)
        self.sum_li = [li[0]]
        for i in range(1, self.n):
            self.sum_li.append(self.sum_li[i-1] + li[i])

    def sum(self, a, b=None):
        if b is None:
            return self.sum(0, a)

        res = self.sum_li[min(self.n-1, b-1)]
        if a > 0:
            res -= self.sum_li[a-1]
        return res

MOD = 1000000007

def mod_add(a, b):
  return (a+b)%MOD

def mod_sub(a, b):
  return (a+MOD-b)%MOD

def mod_mul(a, b):
  return a*b%MOD

#互いに素なa,bについて、a*x+b*y=1の一つの解
def extgcd(a,b):
    r = (1,0,a)
    w = (0,1,b)
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    return (w[0],w[1])

def mod_inv(a):
    x,_ = extgcd(a, MOD)
    return (MOD+x%MOD)%MOD

def mod_div(a, b):
    return a*mod_inv(b)%MOD

def mod_pow(a, b):
    res = 1
    while b > 0:
        if b & 1:
            res = res * a % MOD
        a = a * a % MOD
        b >>= 1
    return res

n, a, b = l_in()

res = mod_pow(2, n)
nCa = 1
for i in range(n, n-a, -1):
    nCa = mod_mul(nCa, i)
for i in range(1, a+1):
    nCa = mod_div(nCa, i)

nCb = 1
for i in range(n, n-b, -1):
    nCb = mod_mul(nCb, i)
for i in range(1, b+1):
    nCb = mod_div(nCb, i)

# print(res, nCa, nCb)

res = mod_sub(res, 1)
res = mod_sub(res, nCa)
res = mod_sub(res, nCb)
print(res)

