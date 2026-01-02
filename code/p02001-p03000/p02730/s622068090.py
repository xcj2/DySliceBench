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


def f(S):
    for s, t in zip(S, S[::-1]):
        if s != t:
            return False
    return True

def main():
    S = input().strip()
    FS = S[:len(S)// 2]
    BS = S[len(S) // 2 + 1:]
    
    if f(S) and f(FS) and f(BS):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()