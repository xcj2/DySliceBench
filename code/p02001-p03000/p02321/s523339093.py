import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_H&lang=ja
# 全列挙する関数
def allp(aa):
    now = [(0, 0)]
    for v, w in aa:
        nxt = [(w + w0, v + v0) for w0, v0 in now]
        now += nxt
    # wでソート
    now.sort(key=lambda x: (x[0], -x[1]))
    # wが昇順ならvも昇順でないと、無駄な組み合わせがあるということなので
    # それを除いて、wとvを別々に返す
    pv = -1
    ww = []
    vv = []
    for w, v in now:
        if v <= pv: continue
        ww.append(w)
        vv.append(v)
        pv = v
    return vv, ww

def main():
    n, wn = MI()
    vw = [LI() for _ in range(n)]
    # 半分全列挙する
    vv1, ww1 = allp(vw[:n // 2])
    vv2, ww2 = allp(vw[n // 2:])
    # 前半は1つずつ動かして、後半はできるだけ動かさない
    # wの和が制限を越えたら後半は動かす
    ans = 0
    j = len(vv2) - 1
    for v1, w1 in zip(vv1, ww1):
        while w1 + ww2[j] > wn:
            if j == 0:
                print(ans)
                exit()
            else:
                j -= 1
        if v1 + vv2[j] > ans: ans = v1 + vv2[j]
    print(ans)

main()

