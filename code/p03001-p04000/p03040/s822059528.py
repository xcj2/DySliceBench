class MultiSet:
    def __init__(self, n):
        self.N = n
        self.n = 1<<n.bit_length()
        self.data = [0] * (self.n + 1)
        self.num = 0
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s
    def add(self, i, x):#iをx個追加
        while i <= self.n:
            self.data[i] += x
            i += i & -i
        self.num+=1
    def search(self, k):#k番目の数を取得
        if k<1:
            return 0
        if k >self.num:
            return self.N+1
        x,sx = 0,0
        step = self.n
        while step:
            y = x+step
            sy = sx+self.data[y]
            if sy < k:
                x,sx = y,sy
            step >>= 1
        return x+1
    def show(self):#debug用
        res = []
        for i in range(1, self.N+1):
            c = self.sum(i)-self.sum(i-1)
            for _ in range(c):
                res.append(i)
        return res
class BIT:
    def __init__(self, n):
        self.N = n
        self.n = 1<<n.bit_length()
        self.data = [0] * (self.n + 1)
        self.S = 0
        
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        self.S+=x
        while i <= self.n:
            self.data[i] += x
            i += i & -i
import bisect
Q = int(input())
compress_list = []
query = []
for _ in range(Q):
    c, *ab = map(int, input().split())
    if c == 1:
        a, b = ab
        compress_list.append(a)
        query.append((c, a, b))
    else:
        query.append([c])
compress_list.sort()
M = MultiSet(len(compress_list))
B = BIT(len(compress_list))
S = 0
for q in query:
    if q[0] == 1:
        a, b = q[1], q[2]
        S+=b
        i = bisect.bisect_right(compress_list, a)
        M.add(i, 1)
        B.add(i, a)
    else:
        if M.num%2 == 0:
            k = M.num//2
            i = M.search(k)
            n1 = M.sum(i-1)
            x = compress_list[i-1]
            s = B.S
            s1 = B.sum(i-1)+(k-n1)*x
            s2 = s-s1
            f = s2-s1+S
        else:
            k = M.num//2+1
            i = M.search(k)
            n1 = M.sum(i-1)
            x = compress_list[i-1]
            s = B.S
            s1 = B.sum(i-1)+(k-n1)*x
            s2 = s-s1
            f = s2-s1+x+S
        print(x, f)










