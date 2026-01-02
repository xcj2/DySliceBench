from bisect import bisect_left, bisect_right

def count(x, li1, li2, p):
    cnt = 0
    now = len(li2)-1 if p else 0
    for ind, i in enumerate(li1):
        rng = range(now, -1, -1) if p else range(now, len(li2))
        for j in rng:
            if p and ind==j:
                continue
            if i*li2[j]<x:
                # print(cnt, ind, j)
                cnt += j+1 if p else len(li2)-j
                cnt -= 1 if p and ind<j else 0
                now = j
                break
        else:
            break
    return cnt//2 if p else cnt

def bisect(ok, ng, solve):
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok

def p_solve(x):
    tmp = count(x, posi, posi, True)
    tmp += count(x, nega[::-1], nega[::-1], True)
    # print(x, tmp)
    return np*nn+nn*nz+nz*np+nz*(nz-1)//2+tmp < k

def n_solve(x):
    return count(x, nega, posi, False) < k


n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
nega = a[:bisect_left(a, 0)]
posi = a[bisect_right(a, 0):]
np = len(posi)
nn = len(nega)
nz = n - np - nn
if k <= np*nn:
    ans = bisect(nega[0]*posi[-1]-1, 0, n_solve)
elif k <= np*nn+nn*nz+nz*np+nz*(nz-1)//2:
    ans = 0
else:
    ma = 0
    if len(nega)>1:
        ma = nega[0]*nega[1]
    if len(posi)>1 and ma<posi[-1]*posi[-2]:
        ma = posi[-1]*posi[-2]
    ans = bisect(1, ma+1, p_solve)
print(ans)
