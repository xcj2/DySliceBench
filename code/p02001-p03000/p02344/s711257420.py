#!python3

import sys
sys.setrecursionlimit(1000000000)
iim = lambda: map(int, input().rstrip().split())

def resolve():
    N, Q = iim()
    S = [i for i in range(N)]
    W = [0] * N
    R = [0] * N

    def find(x):
        if S[x] == x:
            return x

        i = find(S[x])
        W[x] += W[S[x]]
        S[x] = i
        return i

    def relate(x, y, w):
        i = find(x)
        j = find(y)

        if R[i] < R[j]:
            S[i] = j
            W[i] = w - W[x] + W[y]
        else:
            S[j] = i
            W[j] = -w - W[y] + W[x]
            if R[i] == R[j]:
                R[i] += 1

    def diff(x, y):
        i = find(x)
        j = find(y)

        if i != j: return "?"

        return W[x] - W[y]

    ans = []
    for com, *xyz in (map(int, s.split()) for s in sys.stdin):
        if com == 0:
            relate(*xyz)
        else:
            ans.append(diff(*xyz))
    print(*ans, sep="\n")

if __name__ == "__main__":
    resolve()

