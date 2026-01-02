def e_league():
    import sys
    sys.setrecursionlimit(10**6)
    N = int(input())
    A = [[int(i) - 1 for i in input().split()] for j in range(N)]

    # 各試合に識別番号をつける
    match_num = 0
    identification = [[None] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i < j:
                identification[i][j] = match_num
                match_num += 1

    vertex_max = N * (N - 1) // 2  # 試合数だけ頂点を作る
    # match_allocation[n]: n番の選手はこの要素で指定された試合をする必要がある
    match_allocation = [row for row in A]
    # next_match[n]: n番の試合の後に行わなければならない試合の番号
    next_match = [[] for _ in range(vertex_max)]

    def to_id(i, j):
        if i > j:
            i, j = j, i
        return identification[i][j]

    # 上で定義したリストの要件を満たすように値を入れていく
    for i in range(N):
        for j in range(N - 1):
            match_allocation[i][j] = to_id(i, match_allocation[i][j])
        for j in range(N - 2):
            next_match[match_allocation[i][j]].append(match_allocation[i][j + 1])

    # ここから、グラフはDAGか？　DAGなら最長パスはいくらか？
    # 最長パスの長さが解になるようにグラフを作っている
    is_visited = [False] * vertex_max
    is_calculated = [False] * vertex_max
    dp = [0] * vertex_max  # dp[v]: 頂点vからの最大パス長

    def dfs(v):
        if is_visited[v]:
            # 計算結果が確定していない頂点に再度訪れた→DAGじゃない
            if not is_calculated[v]:
                return -1
            return dp[v]

        is_visited[v] = True
        dp[v] = 1
        for u in next_match[v]:
            ret = dfs(u)
            if ret == -1:
                return -1  # vから先でDAGじゃないところがあった
            dp[v] = max(dp[v], ret + 1)  # v-u間の分、+1
        is_calculated[v] = True  # ここでようやく結果が確定
        return dp[v]

    ans = 0
    for v in range(match_num):
        res = dfs(v)
        if res == -1:
            return -1
        ans = max(ans, res)
    return ans

print(e_league())