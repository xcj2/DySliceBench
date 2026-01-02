class RemovableHeap:
    def __init__(self, is_max_heap: bool=False, data :list=None):
        self.data = [] if data is None else data
        self.erased = []
        self.sign = -1 if is_max_heap else 1
    
    def normalize(self):
        while len(self.erased) > 0 and self.data[0] == self.erased[0]:
            heappop(self.data)
            heappop(self.erased)
    
    def pop(self):
        ret = self.sign * heappop(self.data)
        self.normalize()
        return ret

    def push(self, x):
        heappush(self.data, self.sign * x)
        self.normalize()
    
    def remove(self, x):
        heappush(self.erased, self.sign * x)
        self.normalize()
    
    def __len__(self):
        return max(len(self.data) - len(self.erased), 0)
    
    def get(self):
        return self.sign * self.data[0]


def main():
    from sys import setrecursionlimit, stdin, stderr
    from os import environ
    from collections import defaultdict, deque, Counter
    from math import ceil, floor
    from itertools import accumulate, combinations, combinations_with_replacement
    from heapq import heapify, heappop, heappush
    setrecursionlimit(10**6)
    dbg = (lambda *something: stderr.write("\033[92m{}\033[0m".format(str(something)+'\n'))) if 'TERM_PROGRAM' in environ else lambda *x: 0
    input = lambda: stdin.readline().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    P = 10**9+7
    INF = 10**18+10

    N,K = LMIIS()
    A = LMIIS()
    def f(x):
        if x == 0:
            return False
        count = 0
        for a in A:
            count += ceil(a/x) -1
        return count <= K
    
    ng = 0
    ok = 10**9+1
    while ok - ng > 1:
        dbg(ng,ok)
        m = (ng+ok)//2
        if f(m):
            ok = m
        else:
            ng = m
    print(ok)

    
main()