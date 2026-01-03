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
A = LI()

a1 = 0
s1 = 0
for i in range(N):
    s1 += A[i]
    if i % 2 == 0:
        if s1 <= 0:
            a1 += 1-s1
            s1 = 1
    else:
        if s1 >= 0:
            a1 += 1+s1
            s1 = -1
a2 = 0
s2 = 0
for i in range(N):
    s2 += A[i]
    if i % 2 == 1:
        if s2 <= 0:
            a2 += 1-s2
            s2 = 1
    else:
        if s2 >= 0:
            a2 += 1+s2
            s2 = -1

print(min(a1,a2))
