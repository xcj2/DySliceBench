class BinaryIndexedTree:
    def __init__(self, size):
        self.data = [0] * (size+1)
        self.size = size+1
        self.msb = 1 << (size.bit_length()-1)
    
    def _add(self, i, w):
        i += 1
        while i < self.size:
            self.data[i] += w
            i += i & -i
    
    def _get_sum(self, i):
        res = 0
        while i > 0:
            res += self.data[i]
            i -= i & -i
        return res

    def __getitem__(self, i):
        """
        [0,i)
        """
        if isinstance(i, slice):
            if i.start is None:
                return self._get_sum(i.stop)
            else:
                return self._get_sum(i.stop) - self._get_sum(i.start)
        else:
            return 0 # fake value
    
    __setitem__ = _add
    
    def bisect_left(self, v):
        """
        return smallest i s.t v <= sum[:i]
        """
        i = 0
        k = self.msb
        while k > 0:
            i += k
            if i < len(self.data) and self.data[i] < v:
                v -= self.data[i]
            else:
                i -= k
            k >>= 1
        return i
    
    def bisect_right(self, v):
        """
        return smallest i s.t v < sum[:i]
        """
        i = 0
        k = self.msb
        while k > 0:
            i += k
            if i < len(self.data) and self.data[i] <= v:
                v -= self.data[i]
            else:
                i -= k
            k >>= 1
        return i
    
    bisect = bisect_right



def solve(C, queries):
    N = len(C)
    Q = len(queries)
    bit = BinaryIndexedTree(N)

    last_ind = [None]*(N + 1)
    sorted_qi = sorted(range(Q), key=lambda i:queries[i][1])

    res = [None]*Q
    pr = 0
    temp = 0
    for qi in sorted_qi:
        l,r = queries[qi]
        for j,c in enumerate(C[pr:r],start=pr):
            if last_ind[c] is not None:
                bit._add(last_ind[c], -1)
            else:
                temp += 1
            last_ind[c] = j
            bit._add(j, 1)

        pr = r
        res[qi] = temp - bit._get_sum(l-1)

    return res

# from random import randrange, seed
# from time import perf_counter

# def test():
#     seed(1234)
#     N = 5*10**5
#     C = [randrange(N) for _ in range(N)]
#     queries = [tuple(sorted((randrange(1,N+1),randrange(1,N+1)))) for _ in range(N)]
#     start = perf_counter()
#     solve(C,queries)
#     stop = perf_counter()
#     print(stop-start)

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

if __name__ == '__main__':
    N,Q = map(int,readline().split())
    C = list(map(int,readline().split()))

    m = map(int,read().split())
    queries = list(zip(m,m))

    print(*solve(C,queries), sep='\n')
    # test()
