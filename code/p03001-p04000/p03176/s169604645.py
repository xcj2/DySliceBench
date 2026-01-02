import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
H = list(map(int,readline().split()))
A = list(map(int,readline().split()))

"""
・最後の高さ -> 価値の総和
・BITでmaxを管理
"""

class BIT():
    def __init__(self, max_n):
        self.size = max_n + 1
        self.tree = [0] * self.size
        
    def __repr__(self):
        return self.tree.__repr__()
        
    def get_max(self,i):
        s = 0
        while i:
            t = self.tree[i]
            if s<t:
                s=t
            i -= i & -i
        return s
 
    def update(self, i, x):
        while i < self.size:
            if self.tree[i] < x:
                self.tree[i] = x
            i += i & -i

bit = BIT(N)

for i,(a,h) in enumerate(zip(A,H),1):
    x = bit.get_max(h)
    bit.update(h,x+a)

answer = bit.get_max(N)
print(answer)