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
    K = int(input())
    
    q = queue.Queue()
    for i in range(1, 10):
        q.put(i)

    r = 9
    for k in range(K):
        a = q.get()
        l = max(0, a % 10 - 1)
        ll = min(10, a % 10 + 2)
        for b in range(l, ll):
            q.put(a * 10 + b)
            r += 1
    print(a)


if __name__ == "__main__":
    main()
