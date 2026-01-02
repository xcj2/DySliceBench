import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

from heapq import heappop, heappush

def main(): 
    N, M = LI()
    B = [[] for i in range(10**5+1)]
    for _ in range(N):
        a, b = LI()
        B[a].append(b)
    
    hq = []
    ans = 0
    for day in range(1, M+1):
        for b in B[day]:
            heappush(hq, -b)
        if not hq:
            continue
        ans += (-heappop(hq))

    print(ans)



main()