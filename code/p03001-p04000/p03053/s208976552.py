import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7

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
    H, W = read_values()
    F = [input().strip() for _ in range(H)]
    A = [False] * (H * W)
    Q = deque() 

    for h in range(H):
        for w in range(W):
            if F[h][w] == "#":
                Q.append((h, w, 0))
                A[h * W + w] = True

    res = V(max)
    while Q:
        h, w, d = Q.popleft()
        res.ud(d)

        for hh, ww in ((h + 1, w), (h - 1, w), (h, w + 1), (h, w - 1)):
            if 0 <= hh < H and 0 <= ww < W:
                if A[hh * W + ww]:
                    continue
                Q.append((hh, ww, d + 1))
                A[hh * W + ww] = True
    
    print(res)


if __name__ == "__main__":
    main()
