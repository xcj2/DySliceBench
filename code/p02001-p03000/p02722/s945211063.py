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

def f(N):
    c = 0
    for n in range(1, int(N ** 0.5) + 1):
        if N % n == 0:
            c += 1
            if n * n != N:
                c += 1
    return c - 1


def main():
    N = int(input())

    res = 0
    res += f(N - 1)

    for n in range(1, int(N ** 0.5) + 1):
        if N % n == 0:
            if n != 1:
                M = N
                while M % n == 0:
                    M //= n
                if M % n == 1:
                    res += 1
        
            if n * n != N:
                n = N // n
                M = N
                while M % n == 0:
                    M //= n
                if M % n == 1:
                    res += 1

    print(res)


if __name__ == "__main__":
    main()
