import sys
def input(): return sys.stdin.readline().strip()
sys.setrecursionlimit(10**9)

def main():
    N, M = map(int, input().split())
    repn = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        repn[a - 1].append(b - 1)
        repn[b - 1].append(a - 1)

    visited = [0] * N
    visited[0] = 1
    ans = [0]

    def stroke(u):
        #print("now={}, vis={}".format(u, visited))
        if visited == [1] * N:
            ans[0] += 1
            return
        for v in repn[u]:
            if visited[v] == 1: continue
            visited[v] = 1
            stroke(v)
            visited[v] = 0

    stroke(0)
    print(ans[0])

if __name__ == "__main__":
    main()
