def solve_m(k, a_m, a_p):
    def syaku(mid):
        """mid以下になる組の数を数える"""
        rm = 0
        cnt = 0
        for lp, num in enumerate(a_p):
            while True:
                if rm >= len(a_m) or num * a_m[rm] > mid :
                    break
                else:
                    rm += 1
            cnt += rm
        return cnt
                
    ok, ng = 1, -10 ** 20
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if syaku(mid) >= k:
            ok = mid
        else:
            ng = mid
    return ok

    
def solve_p(k, a_m, a_p):
    def syaku(mid):
        """mid以下になる組の数を数える"""
        r = len(a_p)
        cnt = 0
        for l, num in enumerate(a_p):
            while True:
                if r == 0 or num * a_p[r - 1] <= mid:
                    break
                else:
                    r -= 1
            cnt += r
            if l <= r - 1:
                cnt -= 1
        r = len(a_m)
        for l, num in enumerate(a_m):
            while True:
                if r == 0 or num * a_m[r - 1] <= mid:
                    break
                else:
                    r -= 1
            cnt += r
            if l <= r - 1:
                cnt -= 1
        return cnt // 2

    a_m = sorted([-num for num in a_m])
    ok, ng = 10 ** 20, -1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if syaku(mid) >= k:
            ok = mid
        else:
            ng = mid
    return ok


n, k = map(int, input().split())
a = list(map(int, input().split()))

cnt_p, cnt_m, cnt_0 = 0, 0, 0
tmp_p, tmp_m, tmp_0 = 0, 0, 0
for num in a:
    if num > 0:
        tmp_p += 1
    elif num < 0:
        tmp_m += 1
    else:
        tmp_0 += 1
cnt_p += tmp_p * (tmp_p - 1) // 2 + tmp_m * (tmp_m - 1) // 2
cnt_m += tmp_p * tmp_m
cnt_0 += (tmp_p + tmp_m) * tmp_0 + tmp_0 * (tmp_0 - 1) // 2
# print(cnt_p, cnt_m, cnt_0)

a_m = sorted([a[i] for i in range(n) if a[i] < 0])
a_p = sorted([a[i] for i in range(n) if a[i] > 0])

if k <= cnt_m:
    ans = solve_m(k, a_m, a_p)
elif cnt_m < k <= cnt_m + cnt_0:
    ans = 0
else:
    ans = solve_p(k - cnt_m - cnt_0, a_m, a_p)
      
print(ans)

