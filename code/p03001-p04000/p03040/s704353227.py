import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
from bisect import insort

class BIT():
 
    def __init__(self, n):
        '''
        n = 要素数
        添字は i = 0 ~ n-1 となる
        '''
        self.n = n
        self.bit = [0] * (n + 1)
 
    def add(self, i, x):
        '''i番目の要素にxを加算する'''
        i = i + 1
        while i <= self.n:
            self.bit[i] += x
            i += i & -i
 
    def _sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s
 
    def get(self, i, j):
        '''[i, j)の和を求める'''
        return self._sum(j) - self._sum(i)
  
def compress(list1):
    list2 = sorted(set(list1))
    memo = {value : index for index, value in enumerate(list2)}
    return memo, len(list2)

q = int(readline())
info = [list(map(int, input().split())) for i in range(q)]
 
#座圧する
li1 = []
for i in range(q):
    if info[i][0] == 1:
        li1.append(info[i][1])
        
memo, len_memo = compress(li1)

def median():
    ok = len_memo
    ng = 0
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if 2 * bit1.get(mid, len_memo) <= cnt :
            ok = mid
        else:
            ng = mid
    return memo_inv[ng]
  
#値を管理するBIT
bit = BIT(len_memo)
#要素数を管理するBITに
bit1 = BIT(len_memo)
memo_inv = dict([(v,k) for k,v in memo.items()])
  
s = 0
cnt = 0
for i in range(q):
  que = info[i]
  if que[0] == 1:
    a,b,c = que
    s += c
    cnt += 1
    bit.add(memo[b],b)
    bit1.add(memo[b], 1)
  else:
    d = median()
    sum1 = bit.get(0, memo[d])
    num1 = bit1.get(0, memo[d])
    sum2 = bit.get(memo[d], len_memo)
    num2 = bit1.get(memo[d], len_memo)
    print(d, abs(num1*d- sum1) + abs(num2*d - sum2) + s)