class BIT:
    def __init__(self, n, init=None):
        self.size = n
        if init is None:
            self.bit = [0] * (n + 1) # don't use bit[0]
        else:
            self.bit = [0] + init
            for i in range(1, n):
                self.bit[i + (i & -i)] += self.bit[i]

    def sum(self, i):
        '''
        Calculate bit[1] + ... + bit[i]
        '''
        S = 0
        while i > 0:
            S += self.bit[i]
            i -= i & -i
        return S

    def add(self, i, x):
        '''
        set bit[i] to be bit[i] + x
        '''
        assert i > 0
        while i <= self.size:
            self.bit[i] += x
            i += i & -i

def coord_compress(A):
    B = {a: i for i, a in enumerate(sorted(set(A)))}
    return [B[a] for a in A]
    
def inversion_number(A):
    inv = 0
    bit = BIT(len(A))
    for i, x in enumerate(coord_compress(A)):
        inv += i - bit.sum(x+1)
        bit.add(x+1, 1)
    return inv

N = int(input())
*A, = map(int, input().split())
print(inversion_number(A))
