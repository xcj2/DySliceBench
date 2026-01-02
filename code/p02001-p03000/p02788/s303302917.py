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
    
    def add(self, co, x):
        i = self.co_to_ind[co]
        while i > 0:
            self.data[i] += x
            i -= i & -i
    
    def now(self, x):
        i = self.co_to_ind[x]
        ret = 0
        while i <= self.max:
            ret += self.data[i]
            i += i & -i
        return ret
    
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

N, D, A = map(int, input().split())
XH = [list(map(int, input().split())) for _ in range(N)]
if D == 0:
    ans = 0
    for x, h in XH:
        ans += (h+A-1)//A
else:
    XH.sort()
    Input = []
    for x, h in XH:
        Input.append(x)

    Input.sort()

    bit = BITbisect(Input)
    ans = 0
    for x, h in XH:
        now = bit.now(x)
        if now >= h: continue
        count = (h-now+A-1)//A
        ans += count
        nx = Input[bisect_right(Input, x+2*D)-1]
        bit.add(nx, A*count)

print(ans)