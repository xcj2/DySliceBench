import sys
from heapq import heappush, heappop
def input(): return sys.stdin.readline().strip()

"""
無向グラフでdpできるのが非直感的だが（というのも普通dpをするのはDAGに限るから）、
まず無向グラフは各辺に対して向きの違う有向辺が２本走っていると思えば一応有向グラフではある。

ダイクストラ自体はacyclicityは要請しないので実行可能だが、このとき各頂点への最短距離を小さい順に並べる。
    （例） S--->A--->B--->C--->D--->E
すると実は元のグラフからA--->SやC--->Bといった上の順番と逆行するような辺を除いてもダイクストラの結果は同じになる。
（というのも負辺は無いので逆向きの辺を使うと経路長が長くなるから）

そもそもダイクストラで最小値を取って更新をかけているのはまさに上のような間引いたグラフを構築しているわけで、これは
まさにDAGになっている。なのでこの上でdpを走らせることも可能。

そしてダイクストラとdpを同時に実行できる点が奇跡なのであって、本問のような一般グラフ上でのDAG生成＆dpを俗に
「拡張ダイクストラ」とも言うらしい。
"""

def main():
    N, M, S = map(int, input().split())
    MAX_S = 50 * N + 1
    repn = [[] for _ in range(N)]
    for _ in range(M):
        u, v, a, b = map(int, input().split())
        repn[u - 1].append((v - 1, a, b))
        repn[v - 1].append((u - 1, a, b))
    coin = []
    for _ in range(N):
        c, d = map(int, input().split())
        coin.append((c, d))

    """
    「最短路問題はダイクストラだが、実質それはdpと見れるらしい。」
    重要になるパラメーターは
        ・頂点　・お金　・時間
    なのでdp[v][s][x]が最初に思いつくが確実にTLE、
    ただし移動にかかるお金は制約が強いので
        dp[v][s] = (頂点vに手持ちs円でたどり着く最小の時間)
    とすればよい。
    このときお金sの状態数は上限50*(N-1)とすれば十分。
    (これだけあれば一切換金が不要なので)

    dpの遷移は「辺を移動」、「換金する」の２つあることに注意。
    この遷移を式にする際にダイクストラを用いる。
    """

    dp = [[float("inf")] * (MAX_S + 1) for _ in range(N)]
    S = min(S, MAX_S)
    q = []

    # heappushの再定義（x時間で頂点vにお金sで行けるかどうか）
    def push(x, v, s):
        if not (s < 0 or dp[v][s] <= x):
            dp[v][s] = x
            heappush(q, (x, v, s))
    
    # initialization
    push(0, 0, S)

    # dijkstra
    while q:
        x, v, s = heappop(q)
        if (dp[v][s] != x): continue # すでに別経路で同じ条件を探索済みの場合は除く。（必須ではないが高速化になる）
        # 両替するとき
        new_x = x + coin[v][1]
        new_s = min(s + coin[v][0], MAX_S)
        push(new_x, v, new_s)
        # 辺を移動するとき
        for u, a, b in repn[v]:
            push(x + b, u, s - a)
    
    # answer
    for v in range(1, N):
        ans = float("inf")
        for s in range(MAX_S):
            ans = min(ans, dp[v][s])
        print(ans)

if __name__ == "__main__":
    main()