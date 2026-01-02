
class BinaryIndexedTree:
    def __init__(self, size):
        size = 1 << (size-1).bit_length()
        self.data = [0] * (size+1)
        self.size = size
    
    def add(self, i, w):
        i += 1
        while i <= self.size:
            self.data[i] += w
            i += i & -i

    def sum(self, i):
        """
        [0,i)
        """
        result = 0
        while i > 0:
            result += self.data[i]
            i -= i & -i
        return result

    __getitem__ = sum

    def lower_bound(self, v):
        """
        return smallest i such that v < sum(data[:i])
        """

        s,pos = 0,0
        N = self.size
        k = N
        while k > 0:
            i = pos+k
            if i <= N:
                x = s+self.data[i]
                if x < v:
                    s = x
                    pos = i
            k >>= 1
        return pos

N = int(input())
S = input()
S = list(ord(c)-ord('a') for c in S)
bits = tuple(BinaryIndexedTree(N) for _ in range(26))

for i,c in enumerate(S):
    bit = bits[c]
    bit.add(i, 1)


def q1(i, c):
    i = int(i)-1
    bit = bits[S[i]]
    bit.add(i,-1)
    c = ord(c)-ord('a')
    bit = bits[c]
    bit.add(i,1)
    S[i] = c
def q2(l,r):
    l,r = int(l)-1,int(r)
    print(sum(bit.sum(r) > bit.sum(l) for bit in bits))


Q = int(input())
for _ in range(Q):
    q,x,y = input().split()

    if q == '1':
        q1(x,y)
    else:
        q2(x,y)
