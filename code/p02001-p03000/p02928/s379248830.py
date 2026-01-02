import bisect

class BinaryIndexedTree:
    # http://hos.ac/slides/20140319_bit.pdf
    def __init__(self, size):
        self._bit = [0 for _ in range(size)]
        self._size = size
 
    def add(self, i, w):
        x = i + 1
        while x <= self._size:
            self._bit[x - 1] += w
            x += x & -x
 
    def sum(self, i):
        ret = 0
        x = i + 1
        while x > 0:
            ret += self._bit[x - 1]
            x -= x & -x
        return ret
 
    def __len__(self):
        return self._size
 
 
def count_inversions(li, max=None):
    if not max:
        max = __builtins__.max(li)
    bit = BinaryIndexedTree(size=max + 1)
    ret = 0
    for i in range(len(li)):
        ret += i - bit.sum(li[i])
        bit.add(li[i], 1)
    return ret

  
n,k = map(int, input().split())
a = list(map(int, input().split()))
sorted_a = sorted(a)
d = 0
tree = [0] * (n+1) 
mod = 10 ** 9 + 7
ans = (count_inversions(a, max=max(a)) * k) % mod

for i in a:
  d += bisect.bisect_left(sorted_a, i)

ans += (d*((k*(k-1))//2)) % mod 
print(ans%mod)