class BinaryIndexedTree:
    def __init__(self, size):
        self.data = [0] * (size+1)
        self.msb = 1 << (size.bit_length()-1)
    
    def _add(self, i, w):
        i += 1
        while i < len(self.data):
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
    bit = BinaryIndexedTree(N)

    last_ind = [None]*(5*10**5 + 1)

    queries = sorted(((r,l-1,i) for i,(l,r) in enumerate(queries)), key=lambda x:x[0])
    qi = 0

    res = [None]*len(queries)

    for i,c in enumerate(C):
        li = last_ind[c]
        if li is not None:
            bit[li] -= 1
        last_ind[c] = i
        bit[i] += 1

        while qi < len(queries) and queries[qi][0] == i+1:
            res[queries[qi][2]] = bit[queries[qi][1]:i+1]
            qi += 1
        if qi == len(queries):
            break

    return res

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

if __name__ == '__main__':
    N,Q = map(int,readline().split())
    C = list(map(int,readline().split()))

    m = map(int,read().split())
    queries = list(zip(m,m))

    print(*solve(C,queries), sep='\n')
