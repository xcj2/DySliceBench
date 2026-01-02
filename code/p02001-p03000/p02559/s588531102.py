import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    class BIT:
        '''
        0-indexed
        '''
        def __init__(self, N):
            self.size = N
            self.tree = [0] * (N + 1)
            self.depth = N.bit_length()

        def _bitsum(self, i):
            ret = 0
            while i:
                ret += self.tree[i]
                i ^= i & -i
            return ret

        # [l,r)の和
        def sum(self, l, r=None):
            if r is None:
                return self._bitsum(l)
            else:
                return self._bitsum(r) - self._bitsum(l)

        # i番目にxを追加
        def add(self, i, x):
            i += 1
            while i <= self.size:
                self.tree[i] += x
                i += i & -i
            return

        def lower_bound(self, x):
            sum_ = 0
            pos = 0
            v = 1 << self.depth
            for i in range(self.depth, -1, -1):
                k = pos + v
                if k <= self.size and sum_ + self.tree[k] < x:
                    sum_ += self.tree[k]
                    pos += v
                v >>= 1
            return pos + 1, sum_
        
    N,Q=MI()
    bit=BIT(N)
    A=LI()
    for i in range(N):
        bit.add(i,A[i])
    
    for _ in range(Q):
        t,p,x=MI()
        if t==0:
            bit.add(p,x)
        else:
            print(bit.sum(p,x))
            
            

main()
