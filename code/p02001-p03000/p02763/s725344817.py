class OR_seg:
    def __init__(self,n,init_val,ide_ele = 0):
        # set_val
        self.ide_ele = ide_ele
        self.n = n
        self.num = 2 ** (self.n - 1).bit_length()
        self.seg = [self.ide_ele] * 2 * self.num
        for i in range(n):
            self.seg[i + self.num - 1] = init_val[i]
            # built
        for i in range(self.num - 2, -1, -1):
            self.seg[i] = self.seg[2 * i + 1] | self.seg[2 * i + 2]

    def update(self,k, x):
        k += self.num - 1
        self.seg[k] = x
        while k + 1:
            k = (k - 1) // 2
            self.seg[k] = self.seg[2 * k + 1] | self.seg[2 * k + 2]

    def add(self,k, x):
        k += self.num - 1
        self.seg[k] += x
        while k + 1:
            k = (k - 1) // 2
            self.seg[k] = self.seg[2 * k + 1] | self.seg[2 * k + 2]



    def query(self,p, q):
        if q <= p:
            return self.ide_ele
        p += self.num - 1
        q += self.num - 2
        res = self.ide_ele
        while q - p > 1:
            if p & 1 == 0:
                res |= self.seg[p]

            if q & 1 == 1:
                res |= self.seg[q]
                q -= 1
            p = p // 2
            q = (q - 1) // 2

        res = res | self.seg[p]|self.seg[q]

        return res
def bit_count(x): #立ってるビットの本数を出力
    n = 0
    while x:
        n += 1
        x &= x-1

    return n

alpha_small_dict = {chr(i):i-97 for i in range(97, 97+26)} #辞書ver
n = int(input())
S = input()
init = [2**alpha_small_dict[x] for x in S]
#print(init)
seg = OR_seg(n,init)
q = int(input())
for i in range(q):
    x,y,z = input().split()
    x,y = int(x),int(y)
    #print(x,y,z)
    if x == 1:
        num = alpha_small_dict[z]
        seg.update(y-1,2**num)
    else:
        z = int(z)
        ans = seg.query(y-1,z)
        print(bit_count(ans))