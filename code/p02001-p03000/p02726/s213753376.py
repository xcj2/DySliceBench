from collections import deque

n, x, y = [int(x) for x in input().split()]
x -= 1
y -= 1
BIG = 65521
ans = {i: 0 for i in range(n)}


def bfs(start_v):
    """ある始点からほかの全点に行くまでの最短距離を求める。"""
    qu = deque()
    qu_append = qu.append
    qu_popleft = qu.popleft
    qu_append(start_v)
    # 始点からvに移動するまでの最短距離: dist[v]
    dist = [BIG] * n

    def push(v, d):
        """始点からvまでの最短距離が算出されていないときに，その距離を保存し，
        キューに頂点vを追加する。"""
        if dist[v] != BIG:
            # 既に訪問済みで距離が求められている。
            return
        dist[v] = d
        qu_append(v)

    push(start_v, 0)

    while len(qu):
        v = qu_popleft()
        # 始点からvの次の頂点へ移動する距離。
        d = dist[v] + 1
        if v < n - 1:
            push(v + 1, d)
        if v > 0:
            push(v - 1, d)
        if v == x:
            push(y, d)
        if v == y:
            push(x, d)

    for i in range(n):
        if dist[i] != 0:
            ans[dist[i]] += 1


def main():
    for i in range(n):
        bfs(i)

    for i in range(1, n):
        print(ans[i] // 2)


if __name__ == '__main__':
    main()

# TLE
