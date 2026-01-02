from bisect import bisect_right, bisect_left
# instead of AVLTree
class BITbisect():
    def __init__(self, InputProbNumbers):
        # 座圧
        self.ind_to_co = [-10**18]
        self.co_to_ind = {}
        for ind, num in enumerate(sorted(list(set(InputProbNumbers)))):
            self.ind_to_co.append(num)
            self.co_to_ind[num] = ind+1
        self.max = len(self.co_to_ind)
        self.data = [0]*(self.max+1)
    
    def __str__(self):
        retList = []
        for i in range(1, self.max+1):
            x = self.ind_to_co[i]
            if self.count(x):
                c = self.count(x)
                for _ in range(c):
                    retList.append(x)
        return "[" + ", ".join([str(a) for a in retList]) + "]"
    
    def __getitem__(self, key):
        key += 1
        s = 0
        ind = 0
        l = self.max.bit_length()
        for i in reversed(range(l)):
            if ind + (1<<i) <= self.max:
                if s + self.data[ind+(1<<i)] < key:
                    s += self.data[ind+(1<<i)]
                    ind += (1<<i)
        if ind == self.max or key < 0:
            raise IndexError("BIT index out of range")
        return self.ind_to_co[ind+1]
    
    def __len__(self):
        return self._query_sum(self.max)
    
    def __contains__(self, num):
        if not num in self.co_to_ind:
            return False
        return self.count(num) > 0
    
    # 0からiまでの区間和
    # 左に進んでいく
    def _query_sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    # i番目の要素にxを足す
    # 上に登っていく
    def _add(self, i, x):
        while i <= self.max:
            self.data[i] += x
            i += i & -i
    
    # 値xを挿入
    def push(self, x):
        if not x in self.co_to_ind:
            raise KeyError("The pushing number didnt initialized")
        self._add(self.co_to_ind[x], 1)
            
    # 値xを削除
    def delete(self, x):
        if not x in self.co_to_ind:
            raise KeyError("The deleting number didnt initialized")
        if self.count(x) <= 0:
            raise ValueError("The deleting number doesnt exist")
        self._add(self.co_to_ind[x], -1)

    # 要素xの個数
    def count(self, x):
        return self._query_sum(self.co_to_ind[x]) - self._query_sum(self.co_to_ind[x]-1)
    
    # 値xを超える最低ind
    def bisect_right(self, x):
        if x in self.co_to_ind:
            i = self.co_to_ind[x]
        else:
            i = bisect_right(self.ind_to_co, x) - 1
        return self._query_sum(i)

    # 値xを下回る最低ind
    def bisect_left(self, x):
        if x in self.co_to_ind:
            i = self.co_to_ind[x]
        else:
            i = bisect_left(self.ind_to_co, x)
        if i == 1:
            return 0
        return self._query_sum(i-1)

import sys
input = sys.stdin.readline
INF = 10**14

N = int(input())
white = [None]*N
blue = [None]*N
for i in range(2*N):
    c, n = map(str, input().rstrip().split())
    if c == "W":
        white[int(n)-1] = i
    else:
        blue[int(n)-1] = i

dp1 = [[0]*(N+1) for _ in range(N+1)]
Indb = BITbisect(list(range(2*N+1)))
for j in reversed(range(N)):
    dp1[N][j] = Indb.bisect_left(blue[j])
    Indb.push(blue[j])
    for i in reversed(range(N)):
        if white[i] < blue[j]:
            dp1[i][j] = dp1[i+1][j] + 1
        else:
            dp1[i][j] = dp1[i+1][j]

dp2 = [[0]*(N+1) for _ in range(N+1)]
Indw = BITbisect(list(range(2*N+1)))
for j in reversed(range(N)):
    dp2[j][N] = Indw.bisect_left(white[j])
    Indw.push(white[j])
    for i in reversed(range(N)):
        if blue[i] < white[j]:
            dp2[j][i] = dp2[j][i+1] + 1
        else:
            dp2[j][i] = dp2[j][i+1]

dp = [[INF]*(N+1) for _ in range(N+1)]
dp[N][N] = 0
for i in reversed(range(N+1)):
    for j in reversed(range(N+1)):
        if i == N:
            if j != N:
                dp[i][j] = dp[i][j+1] + dp1[i][j]
        elif j == N:
            dp[i][j] = dp[i+1][j] + dp2[i][j]
        else:
            dp[i][j] = min(dp[i][j+1]+dp1[i][j], dp[i+1][j]+dp2[i][j])
        
print(dp[0][0])