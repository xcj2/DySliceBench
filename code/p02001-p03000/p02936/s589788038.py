import sys
sys.setrecursionlimit(10 ** 9)
def input(): return sys.stdin.readline().rstrip()

def main():
    N, Q = map(int, input().split())
    ki = [[] for _ in range(N + 1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        ki[a].append(b)
        ki[b].append(a)
    PX = [tuple(map(int, input().split())) for _ in range(Q)]

    ans = [0 for _ in range(N + 1)]
    for p, x in PX:
        ans[p] += x
    visited = set()
    def dfs(i):
        visited.add(i)
        for j in ki[i]:
            if j in visited:
                continue
            ans[j] += ans[i]
            dfs(j)
    dfs(1)
    print(*ans[1:])

if __name__ == '__main__':
    main()
