import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines


def string_to_number(a):
    return 1 << (ord(a) - ord("a"))

class SegmentTree:
    def __init__(self, A):
        self.n = 2**(len(A)-1).bit_length()
        self.identity = 0
        self.seg = [self.identity] * (2 * self.n)
        
        for i, a in enumerate(A):
            self.seg[self.n-1+i] = string_to_number(a)
        for i in range(self.n-2,-1,-1):
            self.seg[i] = self.seg[2*i+1] | self.seg[2*i+2]

            
    def update(self, k, a):
        k += self.n - 1
        self.seg[k] = string_to_number(a)
        while k:
            k = (k - 1) // 2
            self.seg[k] = self.seg[k*2+1] | self.seg[k*2+2]

            
    def query(self, a, b):
        if b == a:
        	return 1
        a += self.n - 1
        b += self.n - 2
        res = self.identity
        while b - a > 1:
            if a & 1 == 0:
                res |= self.seg[a]
            if b & 1 == 1:
                res |= self.seg[b]
                b -= 1
            a = a // 2
            b = (b - 1) // 2
        if a == b:
            res |= self.seg[a]
        else:
            res |= (self.seg[a] | self.seg[b])
        
        return bin(res).count("1")


def main():
    N = int(readline())
    s = readline().strip()
    seg = SegmentTree(list(s))
    #print(seg.seg)

    Q = int(readline())
    for _ in range(Q):
        q, a, b = map(str, readline().split())
        if q == "1":
            seg.update(int(a)-1, b)
        else:
            print(seg.query(int(a)-1, int(b)))


if __name__ == "__main__":
    main()
