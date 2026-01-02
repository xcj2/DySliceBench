#create date: 2020-05-03 21:05

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n, m = na()
    h = na()
    g = [[] for i in range(n)]
    for i in range(m):
        a, b = na()
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    ans = 0
    for i in range(n):
        if len(g[i]) > 0:
            if max(h[gi] for gi in g[i]) < h[i]:
                ans += 1
        else:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()