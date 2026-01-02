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
    a_list = LI()

    # 最小を取り出すのでマイナスにする
    a_list = [-1*a for a in a_list]

    import heapq
    heapq.heapify(a_list)

    for i in range(M):
        mn = heapq.heappop(a_list)
        mn = -1*(-1*mn // 2)
        heapq.heappush(a_list, mn)

    print(-1*sum(list(a_list)))


solve()