from collections import defaultdict
debug = print
def debug(*va): pass

def longest_by_topological_sort(N, nexts, prevs):
    visited = [-1] * N
    max_dist = 0
    que = list(range(N))
    while len(que):
        p = que.pop()
        if visited[p] == -1:
            if all(visited[q] != -1 for q in prevs[p]):
                dist = 0
                for q in prevs[p]:
                    dist = max(dist, visited[q] + 1)
                visited[p] = dist
                max_dist = max(max_dist, dist)
                for n in nexts[p]:
                    que.append(n)
    return max_dist

def test_separate():
    import time
    N = 10**5
    t0 = time.time()
    print(longest_by_topological_sort(N, defaultdict(list), defaultdict(list)))
    print('elapsed', time.time() - t0)

def test_fanout():
    import time
    N = 10**5
    nn, pp = defaultdict(list), defaultdict(list)
    for i in range(1, N):
        nn[0].append(i)
        pp[i].append(0)
    t0 = time.time()
    print(longest_by_topological_sort(N, nn, pp))
    print('elapsed', time.time() - t0)

def test_middle():
    import time
    N = 10**5
    nn, pp = defaultdict(list), defaultdict(list)
    for i in range(1, N):
        # fanout
        nn[0].append(i)
        pp[i].append(0)
        # fanin
        nn[i].append(1)
        pp[1].append(i)
    t0 = time.time()
    print(longest_by_topological_sort(N, nn, pp))
    print('elapsed', time.time() - t0)

if __name__ == '__main__':
    N, M = map(int, input().split())

    nextnodes = [defaultdict(list), defaultdict(list)]
    for i in range(M):
        x, y = map(int, input().split())
        nextnodes[0][x - 1].append(y - 1)
        nextnodes[1][y - 1].append(x - 1)

    max_dist = longest_by_topological_sort(N, nextnodes[0], nextnodes[1])
    print(max_dist)
