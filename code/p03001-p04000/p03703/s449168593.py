from itertools import accumulate as acc
class BIT:
  def __init__(self, n):
    self.N = n+1
    self.bit = [0]*self.N
  
  def bit_sum(self, i):
    s = 0
    i += 1
    while i>0:
      s += self.bit[i]
      i -= i & -i
    return s

  def bit_add(self, i, n):
    i += 1
    while i<self.N:
      self.bit[i] += n
      i += i & -i

N, K, *A = map(int, open(0).read().split())
A = [a-K for a in A]
B = [(b,i) for i, b in enumerate(acc(A))]
bit_B = BIT(N)
B.sort(reverse=True)
ans = sum(c[0]>=0 for c in B)
for b,i in B:
  bit_B.bit_add(i,1)
  ans += bit_B.bit_sum(N-1)-bit_B.bit_sum(i)
print(ans)