import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()
from heapq import heappush, heappop

def main():
    q = II()
    Q = []
    for _ in range(q):
        Q.append(LI())
    lows, highs = [], []
    slow, shigh = 0, 0
    bias = 0
    for q in Q:
        if q[0] == 2:
            odd = -lows[0] if len(highs) != len(lows) else 0
            ans = -lows[0], bias + shigh - slow + odd
            print(*ans)
        else:
            _, a, b = q
            bias += b
            if not lows:
                lows = [-a]
                slow = a
            else:
                if a <= -lows[0]:
                    heappush(lows, -a)
                    slow += a
                    if len(lows) > len(highs) + 1:
                        x = -heappop(lows)
                        heappush(highs, x)
                        slow -= x
                        shigh += x
                else:
                    heappush(highs, a)
                    shigh += a
                    if len(highs) > len(lows):
                        x = heappop(highs)
                        heappush(lows, -x)
                        shigh -= x
                        slow += x
    return

main()