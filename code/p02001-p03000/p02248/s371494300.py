import sys
readline = sys.stdin.readline
write = sys.stdout.write

class KMP:
    def __init__(self, W):
        L = len(W)
        T = [0] * (L+1)
        T[0] = -1
        c = 0
        for p in range(1, L):
            if W[p] == W[c]:
                T[p] = T[c]
            else:
                T[p] = c
                c = T[c]
                while c >= 0 and W[p] != W[c]:
                    c = T[c]
            c += 1
        T[L] = c
        self.T = T
        self.W = W

    def search(self, S):
        W = self.W; T = self.T
        R = []
        LS = len(S); LW = len(W)
        # S[i], W[j]
        i = j = 0
        while i < LS:
            if S[i] == W[j]:
                i += 1; j += 1
                if j == LW:
                    R.append(i-j)
                    j = T[j]
            else:
                j = T[j]
                if j < 0:
                    i += 1
                    j += 1
        return R

def solve():
    T = readline().strip()
    P = readline().strip()
    kmp = KMP(P)
    res = kmp.search(T)
    for p in res:
        write("%d\n" % p)
solve()
