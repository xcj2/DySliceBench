import sys
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return list(map(int, sys.stdin.readline().split()))
def II(): return int(sys.stdin.readline())
def LS(): return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]

def main():
    n, q = LI()
    g = defaultdict(list)
    for i in range(n-1):
        a, b = LI()
        g[a].append(b)
    c = [0 for i in range(n+1)]
    for i in range(q):
        p, x = LI()
        c[p] += x


    d = deque([1])
    while len(d) > 0:
        root = d.pop()
        chs = g[root]
        for ch in chs:
            c[ch] += c[root]
            d.append(ch)

    c = [str(i) for i in c]
    print(' '.join(c[1:]))


if __name__ == '__main__':
    main()