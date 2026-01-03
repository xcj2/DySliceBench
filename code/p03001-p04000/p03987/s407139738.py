import bisect
from collections import defaultdict
class SqrtSet:
    def __init__(self, block_limit=201):
        self.key = []
        self.child = [[]]
        self.block_limit = block_limit
 
    def search_lower(self, key):
        if key is None:
            return None
        ret = None
        i = bisect.bisect_left(self.key, key)
        if i != 0:
            ret = self.key[i - 1]
        block = self.child[i]
        i = bisect.bisect_left(block, key)
        if i != 0:
            ret = block[i - 1]
        return ret
        
    def search_higher(self, key):
        if key is None:
            return None
        ret = None
        i = bisect.bisect_right(self.key, key)
        if i != len(self.key):
            ret = self.key[i]
        block = self.child[i]
        i = bisect.bisect_right(block, key)
        if i != len(block):
            ret = block[i]
        return ret
 
    def insert(self, key):
        i = bisect.bisect(self.key, key)
        block = self.child[i]
        bisect.insort(block, key)
        if len(block) == self.block_limit:
            sep = self.block_limit // 2
            self.key.insert(i, block[sep])
            self.child.insert(i + 1, block[sep + 1:])
            self.child[i] = block[:sep]

def main():
    N = int(input())
    A = [int(i) for i in input().split()]

    # IDX[n] <-> A.index(n)
    IDX = defaultdict(int)
    for idx,a in enumerate(A):
        IDX[a] = idx

    SS = SqrtSet()
    SS.insert(-1)
    SS.insert(N)

    ans = 0
    for n in range(1, N + 1):
        H = SS.search_higher(IDX[n])
        L = SS.search_lower(IDX[n])
        ans += (IDX[n] - L) * (H - IDX[n]) *  n
        SS.insert(IDX[n])

    print(ans)

if __name__ == "__main__":
    main()