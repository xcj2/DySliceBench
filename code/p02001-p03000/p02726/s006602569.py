import sys
import itertools
import queue
input = sys.stdin.readline
sys.setrecursionlimit(100000)
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
        if self.v is None:
            self.v = n
        else:
            self.v = self.f(self.v, n) 


def main():
    N, X, Y = read_values()
    X -= 1
    Y -= 1
    res = [0] * N

    for i in range(N - 1):
        for j in range(i + 1, N):
            d = min(
                j - i,
                abs(X - i) + 1 + abs(Y - j),
                abs(Y - i) + 1 + abs(X - j),
            )

            res[d] += 1

    for r in res[1:]:
        print(r)


if __name__ == "__main__":
    main()
