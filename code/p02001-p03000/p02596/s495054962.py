import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

K = I()
if K % 2 == 0 or K % 5 == 0:
    print(-1)
    exit()
if K % 7 == 0:
    K //= 7

A = [1]
for i in range(K+2):
    A.append((A[-1]*10) % K)

a = 1
i = 1
while True:
    if a % K == 0:
        print(i)
        break
    else:
        a += A[i]
        a %= K
        i += 1
