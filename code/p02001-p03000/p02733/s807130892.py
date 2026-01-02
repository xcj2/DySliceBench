import sys
import itertools
input = sys.stdin.readline
sys.setrecursionlimit(100000)
mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


class v:
    def __init__(self, f):
        self.f = f
        self.v = None
 
    def __str__(self):
        return str(self.v)
 
    def ud(self, n):
        if self.v is None:
            self.v = n
        else:
            self.v = self.f(self.v, n) 

def f(i, H):
    B = format(i, "0" + str(H - 1) + "b")
    R = []
    left = 0
    right = 1
    for b in B:
        if b == "1":
            R.append((left, right))
            left = right
        right += 1
    R.append((left, right))
    
    return R


def g(S, H, W, K, block):
    wl = 0
    wr = 1
    res = 0
    while wr != W + 1:
        T = max(S[hr][wr] - S[hl][wr] - S[hr][wl] + S[hl][wl] for hl, hr in block)
        # print(wl, wr, T)
        if T > K:
            if wr - wl == 1:
                return 10 ** 10

            res += 1
            wl = wr - 1
            continue
        wr += 1
    
    return res + len(block) - 1


def main():
    H, W, K = read_values()
    C = [input() for _ in range(H)]

    S = [[0 for _ in range(W + 1)] for __ in range(H + 1)]
    for h in range(H):
        for w in range(W):
            r = int(C[h][w])
            S[h + 1][w + 1] = S[h][w + 1] + S[h + 1][w] - S[h][w] + r

    r = v(min)
    for i in range(1 << (H - 1)):
        block = f(i, H)
        t = g(S, H, W, K, block)
        r.ud(t)
    
    print(r)
        

if __name__ == "__main__":
    main()