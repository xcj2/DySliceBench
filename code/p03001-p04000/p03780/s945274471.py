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

from collections import Counter

n,k = li()
a = li()

a_ltk = [ai for ai in a if ai < k]
a_ltk.sort(reverse=True)
need = {ai:False for ai in a_ltk}

# 貪欲に足していく
for i in range(len(a_ltk)):
    cur = 0
    stack = []
    for j in range(i,len(a_ltk)):
        cur += a_ltk[j]
        stack.append(a_ltk[j])
        if cur >= k:
            for key in set(stack):
                if need[key]:
                    continue
                else:
                    need[key] = True
            stack.pop()
            cur -= a_ltk[j]

                
cnt = Counter(a_ltk)
ans = 0

for k,v in need.items():
    if not v:
        ans += cnt[k]
        
print(ans)