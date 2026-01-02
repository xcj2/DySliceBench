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


import collections

def first_search(graph, root, actions, ans):
    seen, queue = set([root]), collections.deque([[root, 0],])
    while queue:
        vertex, value = queue.pop()  # popleft: 幅優先探索  /  pop: 深さ優先探索
        ans[vertex] = value + actions[vertex]
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append([node, ans[vertex]])


def main(): 
    N, Q = LI()
    from collections import defaultdict
    edges = defaultdict(list)
    for _ in range(N-1):
        a, b = LI()
        edges[a].append(b)
        edges[b].append(a)
    actions = defaultdict(int)
    for _ in range(Q):
        p, x = LI()
        actions[p] += x

    ans = [0 for _ in range(N+1)]

    first_search(edges, 1, actions, ans)

    print(' '.join([str(i) for i in ans[1:]]))




main()