import sys
import bisect
input = sys.stdin.readline

class Bisect(object):
    def bisect_max(self, reva, func,M):
        ok = 0 # exist
        ng = 4*(10**5) # not exist
        while abs(ok-ng) > 1:
            cnt = (ok + ng) // 2
            if func(cnt,reva,M):
                ok = cnt
            else:
                ng = cnt
        return ok

    def bisect_min(self, reva, func,M):
        ok = 10**5 # exist
        ng = 0 # not exist
        while abs(ok-ng) > 1:
            cnt = (ok + ng) // 2
            if func(cnt,reva,M):
                ok = cnt
            else:
                ng = cnt
        return ok

def solve1(tgt,reva,M):
    res=0
    n = len(reva)
    for i in range(n):
        tmp = bisect.bisect_left(reva,tgt-reva[i])
        tmp = n - tmp
        res += tmp
    if M <= res:
        return True
    else:
        return False

def solve2(tgt):
    print(tgt)
    if tgt > 12:
        return True
    else:
        return False
N,M = map(int,input().split())
a = list(map(int,input().split()))
a.sort(reverse=True)
reva = a[::-1]
bs = Bisect()
Kmax = (bs.bisect_max(reva,solve1,M))

r=[0]
for i in range(N):
    r.append(r[i]+a[i])

res = 0
cnt = 0
t = 0
for i in range(N):
    tmp = bisect.bisect_left(reva,Kmax-reva[N-i-1])
    tmp2 = bisect.bisect_right(reva,Kmax-reva[N-i-1])
    if tmp!=tmp2:
        t = 1
    tmp = N - tmp
    cnt += tmp
    res += tmp*a[i]+r[tmp]
if t==1:
    res -= (cnt-M)*Kmax
print(res)
