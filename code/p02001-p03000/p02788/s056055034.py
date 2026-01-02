from heapq import *
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    n, d, a = MI()
    hp = []
    for _ in range(n):
        x, h = MI()
        heappush(hp, (x, 1, h))
    p = 0
    ans = 0
    while hp:
        x, op, h = heappop(hp)
        if op:
            h -= p
            if h > 0:
                ad = (h + a - 1) // a
                ans += ad
                p += ad * a
                heappush(hp, (x + 2 * d + 1, 0, ad * a))
        else:
            p -= h

    print(ans)

main()
