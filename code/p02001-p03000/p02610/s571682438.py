#!python3

import sys
iim = lambda: map(int, sys.stdin.readline().rstrip().split())
sys.setrecursionlimit(1000000000)

def resolve():
    it = map(int, sys.stdin.read().split())

    T = next(it)
    ans = []
    for i in range(T):
        N = next(it)

        val = 0; a1 = []; a2 = []
        for i, v1, v2 in ((next(it), next(it), next(it)) for i in range(N)):
            diff = v1 - v2
            a, v, diff = (a1, v2, diff) if diff >= 0 else (a2, v1, -diff)
            a.append((diff, i))
            val += v
        a1.sort(reverse=True); a2.sort(reverse=True)

        ls = len(a1)
        vis = [None]*(N+1)
        def root(x):
            if vis[x] == None: return x

            vis[x] = root(vis[x])
            return vis[x]
        def root(x):
            a = []
            while True:
                y = vis[x]
                if y == None:
                    break
                a.append(x)
                x = y
            for i in a:
                vis[i] = x
            return x

        for diff, i in a1:
            j = min(i, ls) - 1
            k = root(j)
            #print(diff, i, j, k,  vis)
            if k < 0: continue
            val += diff
            vis[k] = k - 1


        for diff, i in a2:
            j, v2 = max(i, ls), [[-1]]
            k = root(j)
            #print(diff, i, j, k,  vis)
            if k >= N: continue
            val += diff
            vis[k] = k + 1

        ans.append(val)

    print(*ans, sep="\n")



if __name__ == "__main__":
    resolve()
