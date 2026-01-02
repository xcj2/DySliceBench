import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N,K = MI()
A = LI()

left = 0
right = max(A)  # 可能
while left + 1 < right:
    mid = (left + right)//2
    if sum((A[i]+mid-1)//mid - 1 for i in range(N)) <= K:
        right = mid
    else:
        left = mid
print(right)
