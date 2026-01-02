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

dic = {1: 2,
       2: 5,
       3: 5,
       4: 4,
       5: 5,
       6: 6,
       7: 3,
       8: 7,
       9: 6}

n,m = li()
a = list(li())

use = {}
for ai in a:
    if dic[ai] not in use.keys():
        use.update({dic[ai]: ai})
    else:
        use[dic[ai]] = max(use[dic[ai]], ai)
        
# 最大順
desc = {}
edge = {}
for idx, num in enumerate(sorted(use.values(), reverse=True)):
    desc.update({idx: num})
    edge.update({idx: dic[num]})
    
        
# 遷移
INF = float('inf')
dp = [[-INF]*len(use) for _ in range(n+1)]
dp[0] = [0]*len(use)
for i in range(1, n+1):
    cand = dp[i].copy()
    for idx in range(len(use)):
        if i - edge[idx] < 0:
            continue

        if sum(cand) < sum(dp[i-edge[idx]])+1:
            tmp = dp[i-edge[idx]].copy()
            tmp[idx] += 1
            cand = tmp.copy()
            

        elif sum(cand) == sum(dp[i-edge[idx]])+1:
            tmp = dp[i-edge[idx]].copy()
            tmp[idx] += 1
            
            for orgi, tmpi in zip(cand, tmp):
                if orgi == tmpi:
                    continue
                
                elif orgi > tmpi:
                    break
                
                else:
                    cand = tmp.copy()
                    break
                
    dp[i] = cand
                

ans = ""
for num, cnt in zip(desc.values(), dp[-1]):
    ans = ans + str(num)*cnt
    
print(ans)