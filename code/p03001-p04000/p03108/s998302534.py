
import sys
sys.setrecursionlimit(10**9)


def unite(par, i, j):
    j = get_par(par, j)
    par[j] = get_par(par, i)

def get_par(par, p):
    while par[p] != p:
        p = par[p]
    return par[p]

def resolve():
    n,m = map(int, input().split())
    bridges = [list(map(lambda x: int(x)-1, input().split())) for i in range(m)]

    graph = {}
    # if a not in graph:
    #     graph[a] = {}
    # if b not in graph:
    #     graph[b] = {}
    # graph[a][b] = graph[b][a] = 1
    tmp = n * (n-1) // 2
    ans = [tmp]
    append=ans.append
    cnt = [1 for _ in range(n)]
    par = [i for i in range(n)]

    for i in range(m)[::-1]:
        a,b = bridges[i]
        aa = get_par(par, a)
        bb = get_par(par, b)
        if aa == bb:
            append(tmp)
            continue
        # unite
        tmp -= cnt[aa] * cnt[bb]
        append(tmp)
        if cnt[aa] > cnt[bb]:
            par[bb] = aa
            cnt[aa] += cnt[bb]
        else:
            par[aa] = bb
            cnt[bb] += cnt[aa]

    [print(i) for i in ans[:-1][::-1]]


if __name__ == '__main__':
    resolve()
