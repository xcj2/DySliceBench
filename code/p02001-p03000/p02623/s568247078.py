import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N,M,K = map(int,S().split())
A = LI()
A.reverse()
B = LI()
C = A+B

a = 0
b = N-1
r = sum(A)
ans = 0
while a <= N:
    if r > K:
        a += 1
        r -= C[a-1]
    else:
        ans = max(ans,b-a+1)
        b += 1
        if b < len(C):
            r += C[b]
        else:
            break

print(ans)