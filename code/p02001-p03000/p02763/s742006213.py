import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines


def string_to_number(a):
    return 1 << (ord(a) - 97)

class SegmentTree:
    """
    セグ木は 1-indexed
    """
    def __init__(self, n, initial=0):
        self.offset = 2**(n-1).bit_length()
        self.initial = initial
        self.seg = [self.initial] * (2 * self.offset)


    def build(self, A):
        """
        A: 処理したい配列
        """
        for i, a in enumerate(A, start=self.offset):
            self.seg[i] = string_to_number(a)
        for i in range(self.offset-1,0,-1):
            self.seg[i] = self.seg[i<<1] | self.seg[(i<<1)+1]

            
    def update(self, k, a):
        k += self.offset
        self.seg[k] = string_to_number(a)
        while k:
            k >>= 1
            self.seg[k] = self.seg[k<<1] | self.seg[(k<<1)+1]

            
    def query(self, a, b):
        a += self.offset
        b += self.offset
        res = self.initial
        while a < b:
            if a & 1:
                res |= self.seg[a]
                a += 1
            if b & 1:
                res |= self.seg[b-1]
            a >>= 1
            b >>= 1
        
        return bin(res).count("1")


def main():
    N,s,Q,*q = read().split()
    seg = SegmentTree(int(N))
    seg.build(s)
    #print(seg.seg)

    for t, a, b in zip(*[iter(q)]*3):
        if t == "1":
            seg.update(int(a)-1, b)
        else:
            print(seg.query(int(a)-1, int(b)))


if __name__ == "__main__":
    main()
