#!python3

import sys
iim = lambda: map(int, sys.stdin.readline().rstrip().split())

def resolve():
    it = map(int, sys.stdin.read().split())
    V, E = next(it), next(it)

    ee = [-1] * V
    def find(a):
        q = []
        while ee[a] >= 0:
            q.append(a)
            a = ee[a]
        for i in q:
            ee[i] = a
        return a
    def union(a, b):
        ai = find(a)
        bi = find(b)

        r1, r2 = ee[ai],  ee[bi]
        if r1 > r2:
            ai, bi = bi, ai

        ee[bi] = ai
        if r1 == r2:
            ee[ai] -= 1
    def same(a, b):
        ai = find(a)
        bi = find(b)

        return ai == bi

    ans = 0
    for si, ti, wi in sorted(zip(it, it, it), key=lambda x: x[2]):
        if same(si, ti):
            continue
        ans += wi
        union(si, ti)

    print(ans)

if __name__ == "__main__":
    resolve()

