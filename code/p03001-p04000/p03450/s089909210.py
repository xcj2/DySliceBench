def main():
    """
    N,M:10^6より N^2->NG
    矛盾する情報を見つける
    距離情報の保持

    1-2:1, 2-3:1, 1-3:2 <-OK
    1-2:1, 2-3:1, 1-3:5 <-NG(over)
    1-2:1, 2-3:1, 1-3:1 <-NG(less)
    1-2:1, 2-4:3, 1-3:3 <-OK(2-3:2, 3-4:1)
    1-2:1, 2-4:3, 1-3:5 <-NG

    (Li,Ri,Di)
    人Ri は人Li よりも距離 Di だけ右にいる
    すなわち、xRi − xLi = Di
    Ri > Li のとき(人7の右に人8がいる)処理上問題なし
    Ri < Li のとき(人8の右に人7がいる)場合、
    xLi - xRi = -Di
    """
    N, M = map(int, input().split())
    lrd = [
        tuple(map(int, input().split()))
        for _ in range(M)
    ]

    editorial(N, M, lrd)


def editorial(N, M, lrd):
    import sys
    sys.setrecursionlimit(10 ** 7)

    xs = [None] * N
    graph = [[] for _ in range(N)]
    for l, r, d in lrd:
        graph[l - 1].append((r - 1, d))
        graph[r - 1].append((l - 1, -d))

    def dfs(i):
        # 辺情報がなければ独立
        for j, d in graph[i]:
            if xs[j] is None:
                xs[j] = xs[i] + d
                f = dfs(j)
                if not f:
                    return False
            elif xs[j] - xs[i] != d:
                # 距離が誤情報
                return False

        return True

    for i, x in enumerate(xs):
        if x is None:
            # root以外は、dfsで木を探索するときに座標確定
            # １回で確定しないときは、独立した木が存在する
            # 他の木とは別で考えて良いので、初期座標は0固定で問題ない
            xs[i] = 0
            f = dfs(i)
            if not f:
                print("No")
                return

    print("Yes")

if __name__ == '__main__':
    main()
