from copy import deepcopy
from collections import deque
def main():
    def find(x):
        if par[x] < 0:
            return x
        else:
            par[x] = find(par[x])
            return par[x]
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        else:
            if par[x] > par[y]:
                x, y = y, x
            par[x] += par[y]
            par[y] = x
            return True
    def roots():
        return [i for i, x in enumerate(par) if x < 0]

    n = int(input())
    par = [-1] * n
    uvw = {e:[] for e in range(n)}

    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        uvw[u].append((u, v, w))
        uvw[v].append((v, u, w))
        unite(u, v)
    root_node = roots()[0]
    color = [-1] * n
    color[root_node] = 0
    node_next = deque()
    node_next.append(root_node)
    node_next_next = deque()
    node_seen = set()

    while len(node_seen) < n:
        while node_next:
            node_togo = node_next.popleft()
            if node_togo in node_seen:
                continue
            else:
                node_seen.add(node_togo)
            # 次の層のノード群情報を取得し、「次にみるノードlist」にいれる。
            node_adj = uvw[node_togo]
            node_next_next += [i[1] for i in node_adj]
            # 次の層を処理＝色塗りする
            for adj in node_adj:
                if adj[1] in node_seen or color[adj[1]] != -1:
                    continue
                if adj[2] % 2 == 0:
                    color[adj[1]] = color[node_togo]
                else:
                    color[adj[1]] = color[node_togo] ^ 1
        node_next = deepcopy(node_next_next)
        node_next_next = deque()
    print(*color, sep='\n')


if __name__ == '__main__':
    main()
