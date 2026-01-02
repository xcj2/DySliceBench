import bisect
import sys
import itertools
import queue
input = sys.stdin.readline
sys.setrecursionlimit(100000)
# mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


class V:
    def __init__(self, f, v=None):
        self.f = f
        self.v = v
 
    def __str__(self):
        return str(self.v)
 
    def ud(self, n):
        if n is None:
            return

        if self.v is None:
            self.v = n
            return
        self.v = self.f(self.v, n) 


def main():
    N, K, C = read_values()
    S = input().strip()
    P = []

    c = -1
    for i, s in enumerate(S):
        if s == "o":
            if c == -1:
                c = 0
                L = [i]
            else:
                L.append(i)
        if c == -1:
            continue
        c += 1
        if c > C:
            P.append(L)
            c = -1
    if c != -1:
        P.append(L)

    if len(P) > K:
        return

    t = len(P[-1])
    res = []
    for i in range(len(P) - 1, 0, -1):
        if len(P[i][:t]) == 1:
            res.append(str(P[i][0] + 1))
        
        p = P[i][t - 1]
        t = bisect.bisect_left(P[i - 1], p - C)
    
    if len(P[0][:t]) == 1:
        res.append(str(P[0][0] + 1))

    print("\n".join(res[::-1]))


if __name__ == "__main__":
    main()
