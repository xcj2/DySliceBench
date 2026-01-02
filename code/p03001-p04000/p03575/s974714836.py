
from collections import deque

def read_input():
    n, m = map(int, input().split())

    edges = []
    for i in range(m):
        a, b = map(int, input().split())
        edges.append((a, b))

    return n, m, edges


def check_graph(n, edges):
    nodes = list(range(1, n + 1))
    nodes.sort()

    trans = {i: [] for i in nodes}
    for e in edges:
        trans[e[0]].append(e[1])
        trans[e[1]].append(e[0])

    node_q = deque()
    node_q.appendleft(nodes[0])
    searched = []
    while len(node_q) > 0:
        curr = node_q.popleft()
        searched.append(curr)
        target = trans[curr]

        for t in target:
            if t not in searched:
                node_q.appendleft(t)

        searched = list(set(searched))
        searched.sort()

    if searched == nodes:
        return True
    else:
        return False


def submit():
    n, m, edges = read_input()

    count = 0
    for t in range(m):
        test = [e for i, e in enumerate(edges) if i != t]
        if check_graph(n, test):
            count += 1

    print(m - count)

if __name__ == '__main__':
    submit()