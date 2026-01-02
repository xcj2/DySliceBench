# Binary Indexed Tree (Fenwick Tree)
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

      
def solve():
    ok = len_memo
    ng = 0
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if 2 * bit1.get(mid, len_memo) <= cnt :
            ok = mid
        else:
            ng = mid
    return memo_inv[ng]
    

def compress(list1):
    list2 = sorted(set(list1))
    memo = {value : index for index, value in enumerate(list2)}
    #for i in range(len(list1)):
    #    list1[i] = memo[list1[i]]
    return memo, len(list2)

q = int(input())
info = [list(map(int, input().split())) for i in range(q)]

#座圧する
li1 = []
for i in range(q):
    if info[i][0] == 1:
        li1.append(info[i][1])

memo, len_memo = compress(li1)
memo_inv = dict([(v,k) for k,v in memo.items()])
#print(memo)
#print(memo_inv)

#値を管理するBIT
bit = BIT(len_memo)
#要素数を管理するBITに
bit1 = BIT(len_memo)

x = []
b = 0
cnt = 0
for i in range(q):
    if info[i][0] == 1:
        bit.add(memo[info[i][1]], info[i][1])
        bit1.add(memo[info[i][1]], 1)
        b += info[i][2]
        cnt += 1
    if info[i][0] == 2:
        median_x = solve()
        sum1 = bit.get(0, memo[median_x])
        num1 = bit1.get(0, memo[median_x])
        sum2 = bit.get(memo[median_x], len_memo)
        num2 = bit1.get(memo[median_x], len_memo)
        #print(median_x, sum1,num1, sum2, num2)
        print(median_x, abs(num1*median_x - sum1) + abs(num2*median_x - sum2) + b)
