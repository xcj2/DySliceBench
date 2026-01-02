import sys
input = sys.stdin.readline
from bisect import bisect_left

class SegTree:
    def __init__(self, a):
        self.padding = -float('inf')
        self.n = len(a)
        self.N = 2 ** (self.n - 1).bit_length()
        self.data = [self.padding]*(self.N - 1) + a + [self.padding]*(self.N - self.n)
        for i in range(2 * self.N - 2, 0, -2):
            self.data[(i - 1) // 2] = max(self.data[i], self.data[i - 1])
    
    def __len__(self):
        return self.n
    
    def __getitem__(self, key):
        return self.data[self.N - 1 + key]

    def __setitem__(self, i, value):
        self._update(i, value)
    
    def _update(self, i, x):
        idx = self.N - 1 + i
        self.data[idx] = x
        while idx != 0:
            idx = (idx - 1) // 2
            self.data[idx] = max(self.data[2 * idx + 1], self.data[2 * idx + 2])
    
    def max(self, i, j):
        # [i, j)
        if i == j: #今回のみの措置
            return self.data[self.N - 1 + i]
        else:
            idx1 = self.N - 1 + i
            idx2 = self.N - 2 + j # 閉区間にする
            result = self.padding
            while idx1 + 1 < idx2:
                if idx1 % 2 == 0: # idx1が偶数
                    result = max(result, self.data[idx1])
                if idx2 % 2 == 1: # idx2が奇数
                    result = max(result, self.data[idx2])
                    idx2 -= 1
                
                idx1 //= 2
                idx2 = (idx2 - 1)//2
            
            if idx1 == idx2:
                result = max(result, self.data[idx1])
            else: # idx1 + 1 == idx2
                result = max(result, self.data[idx1], self.data[idx2])
            
            return result

n = int(input())
x_d = []
for _ in range(n):
    x_d.append(tuple(map(int, input().split())))
x_d.sort(key=lambda t: t[0])
x = [t[0] for t in x_d]
xplusd = [t[0] + t[1] for t in x_d]
shortright = [bisect_left(x, xpdi) for xpdi in xplusd]
right = SegTree([t for t in shortright])
for i in range(n - 1, -1, -1):
    right[i] = right.max(i, right[i])
dp = [None] * n
dp.append(1)
for i in range(n - 1, -1, -1):
    dp[i] = (dp[i + 1] + dp[right[i]]) % 998244353
print(dp[0])