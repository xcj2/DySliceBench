#!python3

import sys
iim = lambda: map(int, sys.stdin.readline().rstrip().split())

def resolve():
    def find(i):
        x = S[i]
        if x < 0:
            return i
        S[i] = find(x)
        return S[i]

    def join(i, j):
        ai = find(i)
        aj = find(j)
        diff = ai - aj
        if diff == 0:
            return
        elif diff > 0:
            ai, aj = aj, ai
        S[ai] += S[aj]
        S[aj] = ai
    def same(i, j):
        ai = find(i)
        aj = find(j)
        return ai == aj
    def size(i):
        return -S[find(i)]

    N, M, K = iim()
    S = [-1] * N
    T = [1] * N
    for i in range(M):
        ai, bi = iim()
        ai -= 1; bi -= 1
        join(ai, bi)
        T[ai] += 1
        T[bi] += 1
        #print(ai, bi, S)

    for i in range(K):
        ai, bi = iim()
        ai -= 1; bi -= 1
        if same(ai, bi):
            T[ai] += 1
            T[bi] += 1
    #print(S)
    #print(T)

    ans = [size(i) - T[i] for i in range(N)]
    print(*ans)


if __name__ == "__main__":
    resolve()
