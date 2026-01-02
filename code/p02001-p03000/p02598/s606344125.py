import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI0(): return map(lambda s: int(s) - 1, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
def LMI0(): return list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, K = MI()
A = LMI()

A.sort(reverse=True)

def split_cnt(L):
    cnt = 0
    for a in A:
        if a <= L:
            break
        cnt += -(-a // L) - 1
    return cnt



l = 0
r = A[0]
while l + 1< r:
    mid = (l + r) // 2
    if split_cnt(mid) <= K:
        r = mid
    else:
        l = mid
print(r)