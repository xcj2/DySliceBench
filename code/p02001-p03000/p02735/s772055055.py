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


def main():
    H, W = read_values()
    F = ["." * (W + 2)] + ["." + input() + "." for _ in range(H)] + ["." * (W + 2)]
    dp = [[10 ** 10 for _ in range(W + 2)] for __ in range(H + 2)]
    dp[1][0] = 0
    dp[0][1] = 0
    for h in range(1, H + 1):
        for w in range(1, W + 1):
            if F[h][w] == ".":
                dp[h][w] = min(dp[h - 1][w], dp[h][w - 1])
            else:
                hr = 0 if F[h - 1][w] == "#" else 1
                wr = 0 if F[h][w - 1] == "#" else 1
                dp[h][w] = min(dp[h - 1][w] + hr, dp[h][w - 1] + wr)
    print(dp[H][W])


if __name__ == "__main__":
    main()