import sys
from operator import itemgetter
input = sys.stdin.readline

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+1)
        self.value = [0]*(n+1)
    
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s
    
    def add(self, i, x):
        # assert i > 0
        self.value[i] += x
        while i <= self.n:
            self.bit[i] += x
            i += i & -i
    
    def subtract(self, i, x):
        self.add(i, -x)
    
    def init(self, n, lis):
        self.n = n
        self.bit = [0]*(n+1)
        self.value = lis
        for i in range(n):
            self.add(i, lis[i])
            
    def get_value(self, i):
        return self.value[i]
    
    def get_sum(self, i, j):
        return self.sum(j) - self.sum(i)
    
    def lower_bound(self, x):#和がx以上になる最小のインデックス
        if x <= 0:
            return  0
        l, r = 0, self.n
        while r-l > 1:
            index = (r+l)//2
            if self.sum(index) >= x:
                r = index
            else:
                l = index
                
        if self.sum(l) >= x:
            return l
        return r
    
    def upper_bound(self, x):#和がx以下になる最大のインデックス
        if x <= 0:
            return  0
        l, r = 0, self.n
        while r-l > 1:
            index = (r+l)//2
            if self.sum(index) <= x:
                l = index
            else:
                r = index
                
        if self.sum(r) <= x:
            return r
        return l

def main():
    n, q = map(int, input().split())
    c = list(map(int, input().split()))
    query = sorted([list(map(int, input().split())) + [i] for i in range(q)], key=itemgetter(1))
    
    bit = BIT(n)
    index = 0
    already = [0]*(n+1)
    ans = [0]*q
    index = 0
    for l, r, i in query:
        while index < r:
            bit.add(index+1, 1)
            if already[c[index]]:
                bit.subtract(already[c[index]], 1)
            already[c[index]] = index+1
            index += 1
            
        ans[i] = bit.get_sum(l-1, r)

    for a in ans:
        print(a)
        
    
    
    
    
if __name__ == "__main__":
    main()
