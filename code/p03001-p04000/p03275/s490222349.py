import math
 
n = int(input())
a = [int(i) for i in input().split(" ")]

m = n * (n + 1) // 2
 
class BIT:
    def __init__(self, n):
        self.t = [0] * (n + 1)
    
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.t[i]
            i -= (i & -i)
        return s
    
    def add(self, i, v):
        while i < len(self.t):
            self.t[i] += v
            i += (i & -i)
            
def count(s):
    s_min = min(s)
    b = BIT(max(s) - s_min + 1)
    t = [0] * len(s)
    for j in range(0, len(s)):
        t[j] = b.sum(s[j] - s_min + 1)
        b.add(s[j] - s_min + 1, 1)
    return sum(t)
            
def bs(l, r):
    if l == r:
        return l
    else:
        h = math.ceil((l + r) / 2)
        
        ab = [-1 if a[i] < h else 1 for i in range(0, n)]
        s = [0] * (n + 1)
        
        for i in range(1, n + 1):
            s[i] = s[i - 1] + ab[i - 1]
            
        if count(s) >= math.ceil(m / 2):
            return bs(h, r)
        else:
            return bs(l, h - 1)
        
print(bs(min(a), max(a)))