import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque, Counter
def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math
INF = 10 ** 20
MOD = 10**9 + 7
# def combmod(n, k, mod=MOD):
#     if k == 0:
#         return 1
#     if k == 1:
#         return n
#     ret = 1
#     for i in range(n - k + 1, n + 1):
#         ret *= i
#         ret %= mod
#
#     for i in range(1, k + 1):
#         ret *= pow(i, mod - 2, mod)
#         ret %= mod
#
#     return ret
#
#
# class Segtree_op():
#     def __init__(self, n):
#         self.size = 1
#         while (n >= 1):
#             self.size = self.size << 1
#             n = n // 2
#
#         self.arr = [self.unit() for i in range(self.size * 2)]
#
#     def op(self, lch, rch):
#         # update min with holding index
#         return lch + rch
#
#     def unit(self):
#         return 0
#
#     def update(self, k, val):
#         k += self.size - 1
#         self.arr[k] = val
#         while (k):
#             k = (k - 1) // 2
#             self.arr[k] = self.op(self.arr[k * 2 + 1], self.arr[k * 2 + 2])
#
#     def query(self, l, r):
#         L = l + self.size
#         R = r + self.size
#         s = self.unit()
#         while L < R:
#             if R & 1:
#                 R -= 1
#                 s = self.op(s, self.arr[R - 1])
#
#             if L & 1:
#                 s = self.op(s, self.arr[L - 1])
#                 L += 1
#             L >>= 1
#             R >>= 1
#         return s
#
# def update_daikou(st, k):
#     st.update(k, (st.query(0,k+1)) % MOD)
    # print(st.arr)
 
def main():
    k = getList()
    nums = getList()
    mn, mx = 2,2
    for num in nums[::-1]:
        mn = num * math.ceil(mn / num)
        mx = num * (mx// num) + num - 1
        tm = (mx // num) * num
        if tm < mn or tm > mx:
          print(-1)
          return
 
    print(mn, mx)
 
if __name__ == "__main__":
    main()
 