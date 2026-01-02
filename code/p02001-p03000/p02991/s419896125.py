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

def main(): 
    N, M = LI()
    graph = []
    from collections import defaultdict
    reversed_graph_dict = defaultdict(list)
    for _ in range(M):
        u, v = LI()
        graph.append([u,v])
        reversed_graph_dict[v].append(u)
    S, T = LI()

    # print(reversed_graph_dict)

    import collections
    def bfs(graph, root):
        seen, queue = set([root]), collections.deque([[root, 0],])
        first_step_seen = set([])
        second_step_seen = set([])
        while queue:
            vertex, tries = queue.popleft()
            tries += 1

            # 三段先を見に行く。
            first_step = graph[vertex]

            second_step = []
            for x in set(first_step) - first_step_seen:
                second_step += graph[x]
            first_step_seen |= set(first_step)

            third_step = []
            for x in set(second_step) - second_step_seen:
                third_step += graph[x]
            second_step_seen |= set(second_step)

            for node in set(third_step):
                if node == S:
                    print(tries)
                    return
                if node not in seen:
                    seen.add(node)
                    queue.append([node, tries])
        print(-1)
        return

    bfs(reversed_graph_dict, T)


main()