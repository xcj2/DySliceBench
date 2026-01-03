# 入力
import sys
stdin = sys.stdin

def li(): return [int(x) for x in stdin.readline().split()]
def li_(): return [int(x)-1 for x in stdin.readline().split()]
def lf(): return [float(x) for x in stdin.readline().split()]
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(ns())
def nf(): return float(ns())

n = ni()
t = li()
a = li()

MOD = 10**9 + 7

# T,A の更新と矛盾を確認
t_modified = [0]*n
a_modified = [0]*n
t_modified[0] = 1
a_modified[-1] = 1
consistent = True

if max(a) != max(t):
    consistent = False

for i in range(n-1):
    if t[i+1] != t[i]:
        t_modified[i+1] = 1
        
        if t[i+1] > a[i+1]:
            consistent = False
            
    if a[i] != a[i+1]:
        a_modified[i] = 1
        
        if a[i] > t[i]:
            consistent = False

# 更新があった点は1通り、無かった点はmin(ti,ai)通りの高さが考えられる      
ans = 1
for i in range(n):
    if t_modified[i] == 0 and a_modified[i] == 0:
        ans = (ans * min(t[i], a[i])) % MOD

if consistent:
    print(ans)
else:
    print(0)