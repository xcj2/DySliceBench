import sys
from heapq import *

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def main():
    def get_group(k):
        g = pd[k]
        if g < 0:
            return k
        gg = get_group(g)
        pd[k] = gg
        return gg

    def merge(j, k):
        g1 = get_group(j)
        g2 = get_group(k)
        if g1 != g2:
            d1 = -pd[g1]
            d2 = -pd[g2]
            if d2 > d1:
                g1, g2 = g2, g1
            pd[g2] = g1
            if d1 == d2:
                pd[g1] -= 1

    hp = []
    n, h, w = map(int, input().split())
    pd = [-1] * (h + w + 2)  # 親(parent)と深さ(depth)。0以上は親。負の場合、そのノードが根で絶対値が深さ。
    pd[0] = -(h + w + 2)
    for _ in range(n):
        r, c, a = map(int, input().split())
        heappush(hp, [-a, r, h + c])
    cnt = h + w
    ans = 0
    while cnt and hp:
        a, r, c = heappop(hp)
        gr = get_group(r)
        gc = get_group(c)
        if gr + gc == 0: continue
        if gr == gc:
            merge(gr, 0)
        else:
            merge(gr, gc)
        ans -= a
        cnt -= 1
    print(ans)

main()
