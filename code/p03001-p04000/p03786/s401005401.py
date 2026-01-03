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
A.sort()


def f(n):
    a = sum(A[i] for i in range(n+1))
    for i in range(n+1,N):
        if a*2 >= A[i]:
            a += A[i]
        else:
            return False
    return True


left = -1  # ng
right = N-1  # ok
while left + 1 < right:
    mid = (left + right)//2
    if f(mid):
        right = mid
    else:
        left = mid
print(N-right)
