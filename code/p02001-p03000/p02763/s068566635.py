class BIT:
    def __init__(self, n):
        """
            data : BIT木データ
            el : 元配列
        """
        self.n = n
        self.data = [0]*(n+1)
        self.el = [0]*(n+1)
    
    """A1 ~ Aiまでの累積和"""
    def Sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & (-i)   #LSB(Least Significant Bit)の獲得:i&(-i)
        return s
    
    """Ai += x"""
    def Add(self, i, x):
        self.el[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i
    
    """Ai ~ Ajまでの累積和"""
    def Get(self, i, j=None):
        if j is None:
            return self.el[i]
        return self.Sum(j) - self.Sum(i)

def ctoi(c):
    return ord(c) - 97

n = int(input())
s = list(input())
q = int(input())

bits = [BIT(n) for _ in range(26)]
ans = []
for i in range(n):
    bits[ctoi(s[i])].Add(i+1, 1)
for _ in range(q):
    line = list(input().split())
    if line[0] == '1':
        idx = int(line[1])
        bits[ctoi(s[idx-1])].Add(idx, -1)
        s[idx-1] = line[2]
        bits[ctoi(line[2])].Add(idx, 1) 
    else:
        l,r = int(line[1]), int(line[2])
        cnt = 0
        for i in range(26):
            if bits[i].Get(l-1,r)!=0:
                cnt += 1
        ans.append(cnt)
for a in ans:
    print(a)