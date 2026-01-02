# 法Pの下での組み合わせ数 nCk を求める
# MAX: nの最大値

P = (10**9)+7

fac=[]
inv=[]
finv=[]

# 拡張ユークリッドアルゴリズム
# (d, x, y): d=ax+by を満たすd, x, yを求める
# aとbが互いに素な整数であればgcd(a,b)=d=1, ax=1 (mod b)
# xは法bの元でaの乗法逆元a^-1になる
def exEuclid(a, b):
    if (b==0):
        return (a, 1, 0)
    else:
        (dd, xx, yy) = exEuclid(b, a % b)
        return (dd, yy, xx - (a//b)*yy)

def COMinit(MAX):
    global fac, inv, finv
    fac=[1 for _ in range(MAX)]
    inv=[1 for _ in range(MAX)]
    finv=[1 for _ in range(MAX)]
    #print('len(fac): {}'.format(len(fac)))
    #print(MAX)
    for i in range(2,MAX):
        #print(i)
        fac[i] = fac[i-1]*i % P
        (d, x, y) = exEuclid(i, P)
        inv[i] = x
        finv[i] = finv[i-1]*inv[i] % P

def COM(n, k):
    if(n<k):
        return 0
    elif ( (n<0)or(k<0)):
        return 0
    else:
        return fac[n]*(finv[n-k]*finv[k] % P) % P

####

#print('x, y:')
x, y = list(map(int,input().split()))
MAX = (x+y)//3 +1  # (X+Y)/3より大きい整数 1 <= X, Y <= 10**6
COMinit(MAX)

if ((x+y)%3 != 0):
    print(0)
    exit()
else:
    n1 = (-x+2*y)//3
    n2 = (2*x -y)//3
    if (n1<0):
        print(0)
        exit()
    elif(n2<0):
        print(0)
        exit()
    else:
        npath = COM(n1+n2, n1)
        print(npath)

