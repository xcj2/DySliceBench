from collections import deque, defaultdict

def read_input():
    n, k, l = map(int, input().split())
    roads = []
    for i in range(k):
        p, q = map(int, input().split())
        roads.append((p, q))

    rails = []
    for j in range(l):
        r, s = map(int, input().split())
        rails.append((r, s))

    return n, k, l, roads, rails


def set_ids(nodes, paths):
    edge_table = {n: [] for n in nodes}

    for p in paths:
        edge_table[p[0]].append(p[1])
        edge_table[p[1]].append(p[0])

    ids = [-1] * (len(nodes) + 1)
    q = deque()
    start = 1
    group = 1
    while True:
        # まだセットしていないnodeを見つける
        while ids[start] != -1:
            start += 1
            if start > len(nodes):
                return ids

        q.appendleft(start)
        while len(q) > 0:
            curr = q.popleft()
            ids[curr] = group

            for node in edge_table[curr]:
                if ids[node] == -1:
                    q.appendleft(node)
        group += 1


def submit():
    n, k, l, roads, rails = read_input()
    nodes = list(range(1, n + 1))

    road_ids = set_ids(nodes, roads)
    rail_ids = set_ids(nodes, rails)

    count = defaultdict(int)
    for node in nodes:
        count[(road_ids[node], rail_ids[node])] += 1

    print(' '.join([str(count[(road_ids[node], rail_ids[node])]) for node in nodes]))


if __name__ == '__main__':
    submit()
