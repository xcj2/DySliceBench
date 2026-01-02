import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")

n,k = map(int, input().split())
a = list(map(int, input().split()))
ma = []
pa = []
zc = 0
for num in a:
    if num<0:
        ma.append(num)
    elif num>0:
        pa.append(num)
    else:
        zc += 1
mn = len(ma)*len(pa)
ma.sort()
pa.sort()
ma =ma[::-1]

def _sub(m, l1):
    lp = len(l1)
    t = lp-1
    ans = 0
    for s in range(lp):
        if t<=s:
            break
        while l1[s]*l1[t]>m and t>s+1:
            t -= 1
        if l1[s]*l1[t]>m:
            break
        ans += (t-s)
    return ans

def sub1(m):
    # 0以上m以下の値の個数
    ans = 0
    ans += _sub(m, pa)
    ans += _sub(m, ma)
    return ans

def sub2(m):
    # 0以下、m以下の値の個数
    ans = 0
    lp = len(pa)
    lm = len(ma)
    t = 0
    for s in reversed(range(lp)):
        while pa[s]*ma[t]>m and t<lm-1:
            t += 1
        if pa[s]*ma[t]>m:
            break
        ans += lm - t
    return ans

znum = zc*(len(ma)+len(pa)) + (zc-1)*zc//2
if k>mn:
    k -= mn
    if znum>=k:
        ans = 0
    else:
        k -= znum
        l = 0
        r = 10**18+1
        while l<r-1:
            m = (l+r)//2
            v = sub1(m)
            if v>=k:
                r = m
            else:
                l = m
        ans = l+1
else:
    l = -10**18-1
    r = 0
    while l<r-1:
        m = (l+r)//2
        v = sub2(m)
        if v>=k:
            r = m
        else:
            l = m
    ans = l+1
print(ans)