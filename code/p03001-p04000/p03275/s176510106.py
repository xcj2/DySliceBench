import math

n = int(input())
lst = list(map(int, input().split()))
 
class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
 
            
def judge(x, lst, n):
 
    length = len(lst)
    all_pair = (length*(length-1) // 2) + length
    
    lst_r = [-1 if i < x else 1 for i in lst]
    lst_accum = []
    a = 0
    for i in lst_r:
        a += i
        lst_accum.append(a)
    
    bit = Bit(n)
    lst_accum_sorted = {b: i for i, b in enumerate(sorted(lst_accum), start=1)}
    count = 0
    for j, b in enumerate(lst_accum):
        count += bit.sum(lst_accum_sorted[b]) + (b >= 0)
        bit.add(lst_accum_sorted[b], 1)
        
    if count >= math.ceil(all_pair/2):
        return True
    else:
        return False
 
    
sorted_lst = sorted(lst)
low = 0
high = len(lst) - 1
while high - low >1:
    t = (low+high) // 2
    i = sorted_lst[t]
    if judge(i, lst, n):
        low = t
    else:
        high = t
        
print(sorted_lst[high]) if judge(sorted_lst[high], lst, n) else print(sorted_lst[low])