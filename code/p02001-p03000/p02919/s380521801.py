
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
            bit.add(i,1)
            c = bit.sum(i)
            
            low1 = -1 if c <= 0 else bit.lower_bound(c)
            low2 = -1 if c <= 1 else bit.lower_bound(c-1)
            up1 = len(P) if c > cnt-1 else bit.lower_bound(c+2)
            up2 = len(P) if c > cnt-2 else bit.lower_bound(c+3)
            yield v*((up1-i)*(low1-low2)+(i-low1)*(up2-up1))
    return sum(it())


if __name__ == '__main__':
    N = int(input())
    P = list(map(int,input().split()))
    print(solve(P))