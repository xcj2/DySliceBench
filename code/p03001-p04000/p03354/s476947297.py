import sys

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

    n,m=map(int, input().split())
    pd = [-1] * (n + 1)  # 親(parent)と深さ(depth)。0以上は親。負の場合、そのノードが根で絶対値が深さ。
    p=list(map(int, input().split()))
    for _ in range(m):
        x,y=map(int, input().split())
        merge(x-1,y-1)
    ans=0
    for i in range(n-1,-1,-1):
        if get_group(i)==get_group(p[i]-1):
            ans+=1
    print(ans)

main()