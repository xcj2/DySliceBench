import sys


def input():
    return sys.stdin.readline().rstrip()


def solve():
    n = int(input())
    c = list(map(lambda x : int(x)-1, input().split()))
    # c = [x-1 for x in c]
    # print(c)
    adj = [[] for i in range(n)]
    for i in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append(b)
        adj[b].append(a)

    # size = [1 for i in range(n)]
    stack = [[] for color in range(n)]
    # in_time = [-1 for i in range(n)]
    # out_time = [-1 for i in range(n)]
    size = [1]*n
    # stack = [[]]*n
    in_time = [-1]*n
    out_time = [-1]*n
    timer = 0
    total = n*(n+1)//2
    # ans = [total for color in range(n)]
    ans = [total]*n
    # print(ans)

    def dfs(parent, root):
        nonlocal timer
        in_time[root] = timer
        timer += 1

        for child in adj[root]:
            if parent == child:
                continue
            dfs(root, child)
            size[root] += size[child]

            cnt = size[child]
            while stack[c[root]]:
                x = stack[c[root]][-1]
                if in_time[x] > in_time[root] and out_time[x] != -1:
                    cnt -= size[x]
                    stack[c[root]].pop()
                else:
                    break
            ans[c[root]] -= cnt*(cnt+1)//2

        out_time[root] = timer
        timer += 1

        stack[c[root]].append(root)

    sys.setrecursionlimit(10**6)

    dfs(0, 0)
    # print(size)
    for color in range(n):
        cnt = n
        while len(stack[color]) > 0:
            x = stack[color][-1]
            cnt -= size[x]
            stack[color].pop()
        # print("node:", -1, "color:", color, "cnt:", cnt)
        ans[color] -= cnt*(cnt+1)//2
        print(ans[color])


solve()
