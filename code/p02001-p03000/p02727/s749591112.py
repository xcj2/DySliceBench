import sys
import itertools
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

def SS(L):
    S = [0] * (len(L))
    for i, l in enumerate(L):
        S[i + 1] = S[i] + l

    return S


def main():
    X, Y, A, B, C = read_values()
    P = sorted(read_list(), reverse=True) + [-1]
    Q = sorted(read_list(), reverse=True) + [-1]
    R = sorted(read_list(), reverse=True) + [-1]

    x = 0
    y = 0
    r = 0

    res = 0
    for _ in range(X + Y):
        a = P[x]
        b = Q[y]
        c = R[r]

        if c >= a and c >= b:
            res += c
            r += 1
            continue
        
        if x == X:
            if c >= b:
                res += c
                r += 1
            else:
                res += b
                y += 1
            continue

        if y == Y:
            if c >= a:
                res += c
                r += 1
            else:
                res += a
                x += 1
            continue

        if a >= b:
            res += a
            x += 1
        else:
            res += b
            y += 1

    print(res)
    
        
if __name__ == "__main__":
    main()
