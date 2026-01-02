import sys
from collections import defaultdict, deque, Counter
import math
 
# import copy
from bisect import bisect_left, bisect_right
# import heapq
 
# sys.setrecursionlimit(1000000)
 
# input aliases
input = sys.stdin.readline
 
getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]
 
INF = 10 ** 20
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)
 
class Segtree_op():
     def __init__(self, n):
         self.size = 1
         while(n >= 1):
             self.size = self.size << 1
             n = n//2
 
         self.arr = [self.unit() for i in range(self.size*2)]
 
     def op(self, lch, rch):
         # update min with holding index
         return lch + rch
 
     def unit(self):
         return 0
 
     def update(self, k, val):
         k += self.size - 1
         self.arr[k] = val
         while(k):
             k = (k - 1) // 2
             self.arr[k] = self.op(self.arr[k*2 + 1], self.arr[k*2 + 2])
 
     def query(self, l, r):
         L = l + self.size
         R = r + self.size
         s = self.unit()
         while L < R:
             if R & 1:
                 R -= 1
                 s = self.op(s, self.arr[R - 1])
 
             if L & 1:
                 s = self.op(s, self.arr[L - 1])
                 L += 1
             L >>= 1
             R >>= 1
         return s
 
 
     def show(self):
         idx = 1
         while(idx <= self.size):
             print(self.arr[idx - 1:idx * 2 - 1])
             idx *= 2
def tento(nums):
    st = Segtree_op(max(nums))
    ret = 0
    for i, num in enumerate(nums):
        st.update(num, st.query(num, num+1)+1)
        # st.show()
        ret += i - st.query(0, num+1) + 1

    return ret



def main():
    n, kk = getList()
    nums = getList()
    ten = tento(nums)
    oneset = 0
    for k, v in Counter(nums).items():
        oneset += (n - v) * v
    # print(ten, oneset)
    print((kk * ten + kk * (kk-1) * oneset // 4)% MOD)

if __name__ == "__main__":
    main()
   