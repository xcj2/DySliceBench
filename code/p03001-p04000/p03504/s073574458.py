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
    import bisect
    N, C = read_values()
    W = read_lists(N)
    W.sort(key=lambda x: x[1], reverse=True)

    R = []
    for s, t, c in W:
        i = bisect.bisect_left(R, (t, -1))

        while i < len(R):
            if R[i][0] != t:
                break
            if R[i][1] == c:
                break
            i += 1

        if i < len(R):
            del R[i]

        bisect.insort(R, (s, c))
    print(len(R))


if __name__ == "__main__":
    main()