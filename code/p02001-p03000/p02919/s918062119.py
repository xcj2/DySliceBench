class BinaryIndexedTree:
    def __init__(self, size):
        self.data = [0] * (size+1)
        self.msb = 1 << (size.bit_length()-1)
    
    def add(self, i, w):
        i += 1
        while i < len(self.data):
            self.data[i] += w
            i += i & -i
    
    def get_sum(self, i):
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
            return self.get_sum(i.stop) if i.start is None else self.get_sum(i.stop) - self.get_sum(i.start)
        else:
            return 0 # fake value
    
    __setitem__ = add
    
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

def naive(P):
    def it():
        for i in range(len(P)-1):
            for j in range(i+1,len(P)):
                yield sorted(P[i:j+1])[-2]
    return sum(it())

def solve(P):

    def it():
        bit = BinaryIndexedTree(len(P))
        for cnt, (v,i) in enumerate(sorted(((v,i) for i,v in enumerate(P)), reverse=True)):
            bit[i] += 1
            c = bit.get_sum(i)
            low1 = -1 if c <= 0 else bit.bisect_left(c)
            low2 = -1 if c <= 1 else bit.bisect_left(c-1)
            up1 = len(P) if c > cnt-1 else bit.bisect_left(c+2)
            up2 = len(P) if c > cnt-2 else bit.bisect_left(c+3)
            yield v*((up1-i)*(low1-low2)+(i-low1)*(up2-up1))
    return sum(it())


if __name__ == '__main__':
    N = int(input())
    P = list(map(int,input().split()))
    print(solve(P))