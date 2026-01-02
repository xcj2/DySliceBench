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

debug = True
debug = False

def dprint(*objects):
    if debug == True:
        print(*objects)

def solve():
    N, M = LI()
    import collections
    ab = collections.defaultdict(list)
    for i in range(N):
        a, b = LI()
        ab[a].append(-1*b)

    dprint(ab)
    import heapq
    sumb = 0
    tgt = []
    heapq.heapify(tgt)

    for i in range(1, M+1):
        b_list = ab[i]
        for b in b_list:
            heapq.heappush(tgt, b)

        dprint(tgt)
        if len(tgt) != 0:
            mn = heapq.heappop(tgt)
            sumb += mn
            dprint(mn, sumb)
        dprint(tgt)

    print(sumb*-1)

solve()