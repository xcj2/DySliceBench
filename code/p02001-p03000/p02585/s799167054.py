# import sys
# input = sys.stdin.readline

def mp(): return map(int, input().split())
def lmp(): return list(map(int, input().split()))

n,k = mp()
p = lmp()
p = [p[i]-1 for i in range(n)]
c = lmp()


def cum_sum(lst):
    cums = [0] * (len(lst)+1)
    cums[1] = lst[0]
    for i in range(2,len(lst)+1):
        cums[i] = cums[i-1] + lst[i-1]
    return cums

ans = -int(1e18)-5
for i in range(n):
    now = p[i]
    sc = [c[now]]
    cnt = 1
    while now != i:
        now = p[now]
        sc.append(c[now])
        cnt += 1
    cums = cum_sum(sc)[1:]
    if k <= len(cums):
        cums = cums[:k]
        ans = max(ans, max(cums))
    else:
        if cums[-1] <= 0:
            ans = max(ans, max(cums))
        else:
            lop = k // len(cums)
            u = [cums[j]+(lop-1)*cums[-1] for j in range(len(cums))] + [cums[j]+lop*cums[-1] for j in range(k%len(cums))]
            ans = max(ans,max(u))
print(ans)


