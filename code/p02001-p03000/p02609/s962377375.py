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

if N == 0:
    print(1)
    exit()

A = [0]*(2*10**5+1)
for i in range(1,2*10**5+1):
    k = 0
    for j in range(18):
        if (i >> j) & 1:
            k += 1
    A[i] = A[i % k] + 1


r = sum(X)

if r >= 2:
    B = [0]*N
    C = [0]*N
    b,c = 0,0
    for i in range(N):
        if i == 0:
            B[i] = 1
            C[i] = 1
            if X[i] == 1:
                b = 1
                c = 1
        else:
            B[i] = (B[i-1]*2) % (r-1)
            C[i] = (C[i-1]*2) % (r+1)
            if X[i] == 1:
                b += B[i]
                b %= r-1
                c += C[i]
                c %= r+1

    for i in range(N-1,-1,-1):
        if X[i] == 1:
            print(1+A[(b-B[i]) % (r-1)])
        else:
            print(1+A[(c+C[i]) % (r+1)])

else:
    C = [0] * N
    c = 0
    for i in range(N):
        if i == 0:
            C[i] = 1
            if X[i] == 1:
                c = 1
        else:
            C[i] = (C[i - 1] * 2) % (r + 1)
            if X[i] == 1:
                c += C[i]
                c %= r + 1

    for i in range(N - 1, -1, -1):
        if X[i] == 0:
            print(1 + A[(c + C[i]) % (r + 1)])
        else:
            print(0)
