def mp(): return map(int, input().split())
def lmp(): return list(map(int, input().split()))

def cum_sum(lst):
    cums = [0] * (len(lst)+1)
    cums[1] = lst[0]
    for i in range(2,len(lst)+1):
        cums[i] = cums[i-1] + lst[i-1]
    return cums


n = int(input())
a = lmp()
ar = list(reversed(a))
amx = [1]
for i in range(n):
    u = (amx[i]-a[i])*2
    if u <= 0:
        print(-1)
        exit()
    else:
        amx.append(u)
arcum = cum_sum(ar)[1:]
arcum = list(reversed(arcum))
# print(amx)
# print(arcum)
if amx[-1] < arcum[-1]:
    print(-1)
    exit()
cnt = 0
for i in range(n+1):
    cnt += min(amx[i],arcum[i])
print(cnt)



