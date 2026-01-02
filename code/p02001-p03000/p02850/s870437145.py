
#%%
import sys
sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())

    g = [[] for _ in range(N-1)]
    for i in range(N-1):
        a, b = map(int, input().split())
        g[a-1].append((b-1, i))

    ans = [[None] for _ in range(N-1)]

    def dfs(v0, c0):
        c = 1
        for v1, e in g[v0]:
            if c==c0:
                c += 1
            ans[e] = c
            if v1 < N-1:
                dfs(v1, c)
            c += 1

    dfs(0, 0)

    print(max(ans))
    for c in ans:
        print(c)



# %%
if __name__ == '__main__':
    main()

# %%
# from atcoder_test import doTest
# doTest("abc146","d",main)
