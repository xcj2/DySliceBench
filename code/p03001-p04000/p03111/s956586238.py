from bisect import bisect, bisect_left
from sys import stdin

def dfs(n):
    l = [0] * n
    ret = []
    def dfs_(n):
        if not n:
            ret.append(l[:])
            return
        for i in ('a', 'b', 'c', '_'):
            l[n-1] = i
            dfs_(n-1)
    dfs_(n)
    return ret

def main():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in [0] * N]

    ans = float('inf')
    for s in dfs(N):
        banboo = {'a': 0, 'b': 0, 'c':0, '_': 0}
        for i, t in enumerate(s):
            banboo[t] += L[i]
        if all((banboo['a'] > 0,
                banboo['b'] > 0,
                banboo['c'] > 0)):
            mp = (s.count('a') + s.count('b') + s.count('c') - 3) * 10
            mp += (abs(banboo['a'] - A) +
                   abs(banboo['b'] - B) +
                   abs(banboo['c'] - C))
            ans = min(ans, mp)
    print(ans)

input = lambda: stdin.readline()
main()
