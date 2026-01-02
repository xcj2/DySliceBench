import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from operator import itemgetter

n = int(readline())
ppp = list(map(int,readline().split()))

def BIT_add(i,x):
    while i <= n:
        tree[i] += x
        i += i&(-i)

def BIT_sum(i):
    s = 0
    while i:
        s += tree[i]
        i -= i&(-i)
    return s

def BIT_search(x):
    # 二分探索。和がx以上となる最小のインデックス(>= 1)を返す
      i = 0
      s = 0
      step = 1<<(n.bit_length()-1)
      while step:
          if i+step <= n and s + tree[i+step] < x:
              i += step
              s += tree[i]
          step >>= 1
      return i+1

q = sorted(enumerate(ppp,1),key=itemgetter(1),reverse=True)
tree = [0]*(n+1)

ans = 0
for i, p in q:
    L = BIT_sum(i) # 左にある既に書き込んだ数の個数
    BIT_add(i,1)
    R = n-p-L # 右にある既に書き込んだ数の個数
    LL = BIT_search(L-1) if L >= 2 else 0
    LR = BIT_search(L) if L >= 1 else 0
    RL = BIT_search(L+2) if R >= 1 else n+1
    RR = BIT_search(L+3) if R >= 2 else n+1
    ans += p*((LR-LL)*(RL-i)+(RR-RL)*(i-LR))
print(ans)