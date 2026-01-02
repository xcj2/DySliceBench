import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

n,k = li()
td = [tuple(li()) for _ in range(n)]

td.sort(key=lambda x:x[1], reverse=True)

kindset = set()
doublestack = []

ans = 0

for ti, di in td[:k]:
    if ti in kindset:
        doublestack.append((ti,di))
    
    else:
        kindset.add(ti)
        
    ans += di

ans += len(kindset) * len(kindset)
score = ans

# n-k個の要素に対して重複を排して交換
for ti, di in td[k:]:
    if ti in kindset:
        continue
    
    # すべてユニークだったら抜ける
    if len(doublestack) == 0:
        break
    
    #スコア再計算
    old_ti, old_di = doublestack.pop()    
    score = score - old_di + di + 2*len(kindset) + 1
    
    # 更新
    ans = max(ans, score)    
    kindset.add(ti)
    
    
print(ans)