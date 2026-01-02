n,k = map(int,input().split())
a = list(map(int,input().split()))
plus = []
minus = []
zero = 0
for i in range(n):
    if a[i] < 0:
        minus.append(-a[i])
    elif a[i] > 0:
        plus.append(a[i])
    else:
        zero += 1
plus.sort()
minus.sort()
p = len(plus)
m = len(minus)
am = p*m
ap = p*(p-1)//2 + m*(m-1)//2
az = n*(n-1)//2 - am - ap
# print(plus,minus)

def binary_search_func(ok, ng, f):
    while(abs(ok - ng) > 1):
        med = (ok + ng) // 2
        if(f(med) == True):
            ok = med
        else:
            ng = med
    return ok

if k <= am:
    def c(x):# ~-xはk個以上あるか？
        res = p*m
        v = 0
        for i in minus[::-1]:
            kk = (x+i-1)//i
            # x以下のやつを引いていく
            while v < p and plus[v] < kk:
                v += 1
            res -= v
        return res >= k

    ok = 0
    ng = 10**18
    ans = -(binary_search_func(ok, ng, c))
    
elif k <= am + az:
    ans = 0

else:
    k -= am + az
    def c(x):# 1~xはk個以上あるか？
        res = 0
        vm = m-1
        for i,ai in enumerate(minus):
            kkm = x//ai
            while vm and minus[vm] > kkm:
                vm -= 1
            if vm > i:
                res += vm - i
        vp = p-1
        for i,ai in enumerate(plus):
            kkp = x//ai
            while vp and plus[vp] > kkp:
                vp -= 1
            if vp > i:
                res += vp - i
        return res >= k
    
    ok = 10**18
    ng = 0
    ans = binary_search_func(ok, ng, c)

print(ans)