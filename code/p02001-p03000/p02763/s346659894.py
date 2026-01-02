from collections import Counter
def snum(x):
    return ord(x)-ord('a')

class Bit:
    def __init__(self, n,ls):
        self.size=n
        self.tree=[[0]*26 for _ in range(n+1)]
        self.ls=['']*(n+1)

    def sum(self, i, j):
        i-=1
        res=[0]*26
        for k in range(26):
            i2=i
            j2=j
            while j2>0:
                res[k] += self.tree[j2][k]
                j2 -= j2&-j2
            while i2>0:
                res[k] -= self.tree[i2][k]
                i2 -= i2&-i2
        return 26-res.count(0)
    
    def add(self, i, x):
        self.ls[i] = x
        while i <= self.size:
            self.tree[i][snum(x)]+=1
            i += i & -i

    def change(self, i, x):
        original = self.ls[i]
        self.ls[i]=x
        while i <= self.size:
            self.tree[i][snum(original)] -= 1
            self.tree[i][snum(x)] += 1
            i += i & -i
        

n = int(input())
s = list(input())
bit=Bit(n,s)

for i in range(n):
    bit.add(i+1, s[i])

q = int(input())
for _ in range(q):
    query, a, b = input().split()
    if query=='1':
        bit.change(int(a),b)
    else:
        print(bit.sum(int(a), int(b)))
