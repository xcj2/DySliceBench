# 解説を見た

def solve(N, t, a, g) -> int:
    import sys

    sys.setrecursionlimit(10 ** 7)

    def calc_dist(init):
        dist = [-1] * N
        dist[init] = 0

        def _calc_dist(curr):
            for next_ in g[curr]:
                if dist[next_] != -1:
                    continue
                dist[next_] = dist[curr] + 1
                _calc_dist(next_)

        _calc_dist(init)
        return dist

    dist_a = calc_dist(a)
    dist_t = calc_dist(t)

    return max(dist_a[v] for v in range(N) if dist_t[v] < dist_a[v]) - 1


if __name__ == '__main__':
    N, t, a = map(int, input().split())
    t -= 1
    a -= 1

    g = tuple(set() for _ in range(N))
    for _ in range(N - 1):
        u, v = (int(x) - 1 for x in input().split())
        g[u].add(v)
        g[v].add(u)

    print(solve(N, t, a, g))

# 青木君からの距離 > 高橋君からの距離 となる頂点Xが目的地の候補
# 青木君と高橋君の共通祖先からの距離は等しいので、
# 共通祖先への距離は、 青木君 > 高橋君 となり、高橋君は必ずXに到達できる
# Xに着いた高橋君は、手前の頂点とXとを行ったり来たりする
# a-t->at-: aが一歩進んだときに高橋君に会う(-は無人のマス目)
# at: tが手前の頂点に移動したときに青木君に会う
# いずれも手前の頂点まで青木君が移動したときにゲームが終わる
# どのXを選んでも、Xの手前でゲームが終わるので、青木君から最も遠いXを選ぶのが最善
# 頂点X: 追いつめられる位置=葉
