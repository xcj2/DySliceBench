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

def main(): 
    # 入力
    N, M = LI()
    es = [[x for x in LI()] for _ in range(M)]
    all_v = list(range(1, N+1))

    # まず、outs, ins を定義する。
    # outs はグラフの関連リスト表記。
    # outs = {node1: [node2, node3, ...], node2: [...], ...}
    # ins は、そのノードに入る辺の本数。
    # ins  = {node1: 1, node2: 2, ...}

    from collections import defaultdict

    outs = defaultdict(list)  # ノードが int なら、[[] for _ in range(n+1)] でもよさそう。
    ins = defaultdict(int)    # ノードが int なら、 [0 for _ in range(n+1)] でもよさそう。
    for from_v, to_v in es:
        outs[from_v].append(to_v)
        ins[to_v] += 1


    # つぎに、探索キューを初期化する。
    # ノードを全探索し、ins が 0 のものを探索キューに入れておく。

    from collections import deque
    q = deque()
    for v in all_v:
        if ins[v] == 0:
            q.append((v, 0))  # node, depth


    # トポロジカルソート本体（要は幅優先探索）

    res = []
    depth_max = 0
    while q:
        v1, depth = q.popleft()
        res.append(v1)
        for v2 in outs[v1]:
            ins[v2] -= 1
            if ins[v2] == 0:
                q.append((v2, depth+1))
                depth_max = max(depth_max, depth+1)


    # # 結果
    # print(res)  # ソート済みリスト

    # # 閉路判定（閉路はあるか？）
    # print(False if len(res) == n else True)  # res の長さがノード数と一致していたら、閉路なし。そうでなければ閉路あり。

    # 最大の深さ：深さの情報も同時に埋め込んでおく（上のコードにはもう埋め込んである）。
    print(depth_max)


main()