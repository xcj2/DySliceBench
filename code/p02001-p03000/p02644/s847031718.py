import sys
from heapq import heappush, heappop
def input(): return sys.stdin.readline().strip()
INF = 10**18
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def main():
    H, W, K = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
    C = [input() for _ in range(H)]

    """
    まずはKの制約がない時を考える。単純なBFSでは明らかに間に合わないが、
    「位置」と「向き」の直積を頂点として扱うのがポイント。
    隣の頂点に同じ向きで移動するのにコスト0、同じ頂点で向きを変えるのにコスト1かかるとして
    辺を張れば、ダイクストラにより計算量O((4HW + 4HW) * log(4HW))で解ける。

    ではKの制約がある時はどうするかというと、コストを(従来のコスト, 直線移動距離)のペアに変更する。
    直線移動距離がKを超えたら従来のコストを１つ繰り上げる。
    このペアによるコストは辞書式順序により全順序構造を持つので同様にダイクストラで扱える。

    さらに実はこのコストはペアで扱わないにすることもでき、
        直線移動のコスト＝1/K
        方向転換のコスト＝切り上げ
    と定めると整数部分が本問で求めるコストになっている。
    少数は少し怖いので実際にはK倍して扱う。
    """

    # 向き付き2次元配列を１次元に押し込める補助関数を用意
    def toId(i, j, v):
        return (i * W + j) * 4 + v

    dist = [INF] * (H * W * 4)
    q = []

    # ダイクストラ更新１回分の補助関数
    def push(i, j, v, x):
        id = toId(i, j, v)
        if dist[id] <= x: return
        dist[id] = x
        heappush(q, (x, id))

    # ダイクストラ
    for v in range(4): push(x1, y1, v, 0)
    while q:
        x, id = heappop(q)
        if dist[id] != x: continue # 途中で値が書き換わっていたら伝搬は無効化する！
        i, j, v = (id // 4) // W, (id // 4) % W, id % 4
        # 方向転換
        push(i, j, (v + 1) % 4, (x + K - 1) // K * K)
        push(i, j, (v + 2) % 4, (x + K - 1) // K * K)
        push(i, j, (v + 3) % 4, (x + K - 1) // K * K)
        # 直進
        ni, nj = i + di[v], j + dj[v]
        if 0 <= ni < H and 0 <= nj < W and C[ni][nj] == '.':
            push(ni, nj, v, x + 1)
    ans = min(dist[toId(x2, y2, v)] for v in range(4))
    if ans == INF: print(-1)
    else: print((ans + K - 1) // K)
    

if __name__ == "__main__":
    main()
