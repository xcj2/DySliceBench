import sys
from collections import deque
from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


INF = 10**17


def main():

    N, M = in_nn()
    LRD = in_nl2(M)

    edge = [[] for _ in range(N)]

    for i in range(M):
        l, r, d = LRD[i]
        l, r = l - 1, r - 1
        edge[l].append((r, d))
        edge[r].append((l, -d))

    v_set = []
    search = [False] * N

    def bfs(N, v0, edge):

        search[v0] = True
        q = deque()
        q.append(v0)

        while q:
            v = q.popleft()
            for nv, _ in edge[v]:
                if not search[nv]:
                    q.append(nv)
                    search[nv] = True

    for i in range(N):
        if not search[i]:
            bfs(N, i, edge)
            v_set.append(i)

    def judge(v0):

        search = defaultdict(lambda: False)
        search[v0] = True

        q = deque()
        q.append(v0)

        pos = defaultdict(lambda: INF)
        pos[v0] = 0

        vs = [v0]

        while q:
            v = q.popleft()
            now_pos = pos[v]
            for nv, dis in edge[v]:
                if pos[nv] == INF:
                    pos[nv] = now_pos + dis
                elif pos[nv] - now_pos != dis:
                    return False
                if not search[nv]:
                    q.append(nv)
                    search[nv] = True
                    vs.append(nv)

        max_pos = -INF
        min_pos = INF
        for tv in vs:
            tp = pos[tv]
            max_pos = max(max_pos, tp)
            min_pos = min(min_pos, tp)

        return max_pos - min_pos <= 10**9 + 1

    ans = 'Yes'
    for v in v_set:
        if not judge(v):
            ans = 'No'

    print(ans)


if __name__ == '__main__':
    main()
