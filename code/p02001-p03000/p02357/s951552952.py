from itertools import accumulate
from collections import deque
class SWAG:
    def __init__(self, operator_M, e_M):
        self.op_M = operator_M
        self.e_M = e_M
        self.q = deque([])
        self.accL = []
        self.accR = e_M
        self.L = self.R = 0

    def build(self,lst):
        self.q = deque(lst)
        self.L = len(lst)
        self.accL = list(accumulate(reversed(self.q),self.op_M))

    def __len__(self):
        return self.L + self.R

    def fold_all(self):
        if self.L: return self.op_M(self.accL[-1],self.accR)
        else: return self.accR

    def append(self,x):
        self.q.append(x)
        self.accR = self.op_M(self.accR,x)
        self.R += 1
    
    def popleft(self):
        if self.L:
            self.accL.pop()
            self.L -= 1
            return self.q.popleft()
        elif self.R:
            self.L,self.R = self.R-1,0
            self.accL = list(accumulate(reversed(self.q),self.op_M))
            self.accR = self.e_M
            self.accL.pop()
            return self.q.popleft()
        else:
            assert 0


# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

n,l,*a = [int(i) for i in read().split()]

q = SWAG(min,10**9)
q.build(a[:l])
ans = [q.fold_all()]
for i in a[l:]:
    q.popleft()
    q.append(i)
    ans.append(q.fold_all())

print(*ans)

