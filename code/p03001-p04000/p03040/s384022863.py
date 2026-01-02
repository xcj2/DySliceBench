import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
        self.depth = n.bit_length()
 
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
 
    def lower_bound(self, x):
        """ 累積和がx以上になる最小のindexと、その直前までの累積和 """
        sum_ = 0
        pos = 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.tree[k] < x:
                sum_ += self.tree[k]
                pos += 1 << i
        return pos + 1
  
def compress(list1):
    list2 = sorted(set(list1))
    memo = {value : index for index, value in enumerate(list2)}
    return memo, len(list2)

q = int(readline())
L = [list(map(int,readline().split())) for i in range(q)]
 
#座圧する
chk = []
for i in range(q):
    if L[i][0] == 1:
        chk.append(L[i][1])
        
memo, len_memo = compress(chk)
memo_inv = dict([(v,k) for k,v in memo.items()])

#値を管理するBIT
bit = Bit(len_memo)
#要素数を管理するBIT
num = Bit(len_memo)
  
s = 0
cnt = 0
for i in range(q):
  que = L[i]
  if que[0] == 1:
    a,b,c = que
    s += c
    cnt += 1
    bit.add(memo[b]+1,b)
    num.add(memo[b]+1,1)
  else:
    d = num.lower_bound((cnt+1)//2)
    m = memo_inv[d-1]
    sum1 = bit.sum(d)
    num1 = num.sum(d)
    sum2 = bit.sum(len_memo)-bit.sum(d)
    num2 = num.sum(len_memo)-num.sum(d)
    print(m,abs(num1*m-sum1)+abs(num2*m-sum2)+s)