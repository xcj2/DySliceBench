import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()

A = [0]
for i in range(1,2*10**5):
    a = 0
    r = i
    for j in range(18):
        a += (i>>j)&1
    r %= a
    if r == 0:
        A.append(1)
    else:
        A.append(1+A[r])

X = LS2()

b = 0
for i in range(N):
    if X[i] == '1':
        b += 1
if b >= 2:
    c = b-1
    d = b+1

    r1 = 0
    r2 = 0

    amari1 = [1]
    amari2 = [1]
    for i in range(1,N):
        amari1.append((amari1[-1]*2) % c)
        amari2.append((amari2[-1]*2) % d)
    amari1.reverse()
    amari2.reverse()
    for i in range(N):
        if X[i] == '1':
            r1 += amari1[i]
            r1 %= c
            r2 += amari2[i]
            r2 %= d
    ANS = []
    for i in range(N):
        if X[i] == '1':
            e = r1
            e -= amari1[i]
            e %= c
            ANS.append(A[e]+1)
        else:
            f = r2
            f += amari2[i]
            f %= d
            ANS.append(A[f]+1)
else:
    d = b + 1
    r2 = 0


    amari2 = [1]
    for i in range(1, N):
        amari2.append((amari2[-1] * 2) % d)
    amari2.reverse()

    for i in range(N):
        if X[i] == '1':

            r2 += amari2[i]
            r2 %= d
    ANS = []
    for i in range(N):
        if X[i] == '1':

            ANS.append(0)
        else:
            f = r2
            f += amari2[i]
            f %= d
            ANS.append(A[f] + 1)


print(*ANS,sep='\n')