import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    # 最短経路問題で使われるアルゴリズムの１つ。
    # グラフ上の全ての頂点間の最短経路を探す
    # 負の閉路（辺の重みの和が負になるような閉路）がない限り、負の辺があっても使える。

    # 負の閉路を持つ場合は'NEGATIVE CYCLE'を、そうでない場合には(i,j)成分に
    # 頂点iから頂点jへの最短経路の距離を格納するdist_listをprintする関数
    def warshall_floyd(v_num, dist_lst):
        # 負の閉路を持つか
        negative_cycle_flag = False

        # 頂点iから頂点jへの経路と、頂点kを経由した場合の経路とを比較して
        # よりコストの合計が小さい方を配列に入れる動的計画法
        for k in range(v_num):
            for i in range(v_num):
                for j in range(v_num):
                    # i→k→jがつながっててしかもi→jルートよりもイケてるなら更新
                    if dist_lst[i][k] != INF and dist_lst[k][j] != INF:
                        if dist_lst[i][j] > dist_lst[i][k] + dist_lst[k][j]:
                            dist_lst[i][j] = dist_lst[i][k] + dist_lst[k][j]

        for v in range(v_num):
            # dist_lstに負の数が格納されているとは、
            # グラフが負の閉路を持つことを意味する
            if dist_lst[v][v] < 0:
                negative_cycle_flag = True

        return dist_lst

    H, W = map(int, input().split())
    # 頂点の数と辺の数
    v_num, e_num = 10, 100

    # 配列dist_lst[a][b]には頂点a,b間の辺のコストを入れておき、
    # a=bの時は0を、a,b間の辺が存在しないときはINFを入れておく。
    INF = 10 ** 20
    dist_lst = [[INF] * v_num for _ in range(v_num)]

    costs = [[i for i in list(map(int, input().split()))] for _ in range(10)]
    for s in range(10):
        for t in range(10):
            dist_lst[s][t] = costs[s][t]

    dist_lst = warshall_floyd(v_num, dist_lst)
    wall = [[i for i in list(map(int, input().split()))] for _ in range(H)]
    cnt = 0
    for h in range(H):
        for w in range(W):
            val = wall[h][w]
            if val != -1:
                cnt += dist_lst[val][1]
    print(cnt)


resolve()
