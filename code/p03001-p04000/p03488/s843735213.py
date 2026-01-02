import sys
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
MOD = 1000000007
def POW(x, y): return pow(x, y, MOD)
def INV(x, m=MOD): return pow(x, m - 2, m)
def DIV(x, y, m=MOD): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()

S = input()
X,Y=LI()

while S and S[0] == 'F':
    S = S[1:]
    X -= 1

isX = True
cur = 0
xs = []
ys = []
for i in range(len(S)):
    if S[i] == 'T':
        if cur:
            if isX:
                xs.append(cur)
            else:
                ys.append(cur)
        isX = not isX
        cur = 0
    elif S[i] == 'F':
        cur += 1

if cur:
    if isX:
        xs.append(cur)
    else:
        ys.append(cur)

X=abs(X)
Y=abs(Y)
xs.sort()
ys.sort()
xss = [0]
yss = [0]
for i in xs:
    xss.append(xss[-1]+i)
for i in ys:
    yss.append(yss[-1]+i)

memo1 = {}
def dp1(x, i):
    if abs(x) > xss[i+1]: return False
    if i < 0: return x == 0
    if (x, i) in memo1: return memo1[(x,i)]
    res = dp1(x - xs[i], i-1) or dp1(x + xs[i], i-1)
    memo1[(x,i)] = res
    return res

memo2 = {}
def dp2(x, i):
    if abs(x) > yss[i+1]: return False
    if i < 0: return x == 0
    if (x, i) in memo2: return memo2[(x,i)]
    res = dp2(x - ys[i], i-1) or dp2(x + ys[i], i-1)
    memo2[(x,i)] = res
    return res


# print(xs, ys)
print('Yes' if dp1(X, len(xs)-1) and dp2(Y, len(ys)-1) else 'No')
