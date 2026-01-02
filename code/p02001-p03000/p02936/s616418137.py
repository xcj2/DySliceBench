import sys

def main():
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline
    n, q = map(int, input().split())
    #n, q = map(int, "4 3".split())
    g = [[] for _ in range(n)]
    for i in range(n-1):
        a, b = map(int, input().split())
        #a, b = map(int, ["1 2", "2 3", "2 4"][i].split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)


    add = [0] * n
    for i in range(q):
        p, v = map(int, input().split())
        #p, v = map(int, ["2 10", "1 100", "3 1"][i].split())
        #dfs(p-1, v)
        add[p-1] += v

    ans = [0] * n
    def dfs(v,p,value): #p: parent of v
        value += add[v]
        ans[v] = value
        for c in g[v]:
            if c == p: continue
            dfs(c,v,value)
    dfs(0, -1, 0)
    """
    def dfs(start, point):
        stack = [start]
        while stack:
            x = stack.pop()
            ans[x] += point
            stack += g[x]
    """

    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    main()
