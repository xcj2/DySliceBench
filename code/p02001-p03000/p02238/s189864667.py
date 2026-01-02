import sys


def input():
    return sys.stdin.readline().rstrip()


def dfs(c, n, G, ans):
    count = c
    for i, flag in enumerate(G[n]):
        if flag == 1 and ans[i][0] == 0:
            count += 1
            ans[i][0] = i + 1
            ans[i][1] = count
            ans[i][2] = dfs(count, i, G, ans)
            count = ans[i][2]
    else:
        return count + 1


def main():
    n = int(input())
    G = [[0] * n for _ in range(n)]
    ans = [[0] * 3 for _ in range(n)]
    for i in range(n):
        u, k, *v = map(int, input().split())
        for j in range(k):
            G[u-1][v[j]-1] = 1

    count = 1
    for i in range(n):
        if ans[i][0] == 0:
            ans[i][0] = i + 1
            ans[i][1] = count
            ans[i][2] = dfs(count, i, G, ans)
            count = ans[i][2] + 1

    for i in range(n):
        print(*ans[i])


if __name__ == '__main__':
    main()
