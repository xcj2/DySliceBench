# import sys
# input = sys.stdin.readline

def mp(): return map(int, input().split())
def lmp(): return list(map(int, input().split()))

n,m,k = mp()
a = lmp()
b = lmp()
a.append(int(1e12))
b.append(int(1e13))
ans = -1

def cum_sum(lst):
    cums = [0] * (len(lst)+1)
    cums[1] = lst[0]
    for i in range(2,len(lst)+1):
        cums[i] = cums[i-1] + lst[i-1]
    return cums

a = cum_sum(a)
b = cum_sum(b)
import bisect
for i in range(len(a)-1):
    can_use = k-a[i]
    if can_use < 0:
        continue
    u = bisect.bisect_right(b, can_use)
    cnt = i + u - 1
    ans = max(ans, cnt)
print(ans)





