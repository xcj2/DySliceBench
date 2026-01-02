import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


N = I()
X = LI2()
X.reverse()

if N == 1 and len(X) == 1 and X[0] == 0:
    print(1)
    exit()


def popcount(n):
    res = 0
    m = n.bit_length()
    for i in range(m):
        res += (n >> i) & 1
    return res


F = [0]*(2*10**5)
for i in range(1,2*10**5):
    F[i] = 1 + F[i % popcount(i)]

a = sum(X)
b = a-1
c = a+1
if a == 1:
    A, C = [1], [1]  # 2冪をa,b,cで割った余り
    xa, xc = 0, 0  # Xをa,b,cで割った余り
    for i in range(N):
        if X[i] == 1:
            xa += A[-1]
            xc += C[-1]
            xa %= a
            xc %= c
        A.append((2 * A[-1]) % a)
        C.append((2 * C[-1]) % c)

    ANS = []
    for i in range(N):
        if X[i] == 1:
            ANS.append(0)
        else:
            ANS.append(1 + F[(xc + C[i]) % c])

    ANS.reverse()
    print(*ANS, sep='\n')
    exit()

A,B,C = [1],[1],[1]  # 2冪をa,b,cで割った余り
xa,xb,xc = 0,0,0  # Xをa,b,cで割った余り
for i in range(N):
    if X[i] == 1:
        xa += A[-1]
        xb += B[-1]
        xc += C[-1]
        xa %= a
        xb %= b
        xc %= c
    A.append((2*A[-1])%a)
    B.append((2*B[-1])%b)
    C.append((2*C[-1])%c)

ANS = []
for i in range(N):
    if X[i] == 1:
        ANS.append(1 + F[(xb-B[i]) % b])
    else:
        ANS.append(1 + F[(xc+C[i]) % c])

ANS.reverse()
print(*ANS,sep='\n')
