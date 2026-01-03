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

def first_search(graph, root, depth_array):
    seen, queue = set([root]), collections.deque([[root, 0],])
    while queue:
        vertex, depth = queue.popleft()  # popleft: 幅優先探索  /  pop: 深さ優先探索
        depth_array[vertex] = depth
        for node, length in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append([node, depth+length])

def main(): 
    N = II()

    from collections import defaultdict
    tree = defaultdict(list)

    for _ in range(N-1):
        a,b,c = LI()
        tree[a].append((b,c))
        tree[b].append((a,c))

    Q, K = LI()

    depth_array = [0 for _ in range(N+1)]
    # K を根とした木だと思って全点の depth を決める。
    first_search(tree, K, depth_array)


    for _ in range(Q):
        x,y = LI()
        print(depth_array[x]+depth_array[y])


main()