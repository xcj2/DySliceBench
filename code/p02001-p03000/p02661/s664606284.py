import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    ABs = [tuple(map(int, input().split())) for _ in range(N)]

    def isOK_LE(X, thre):
        num = 0
        for A, B in ABs:
            if A <= X:
                num += 1
        return num >= thre

    def isOK_GE(X, thre):
        num = 0
        for A, B in ABs:
            if X <= B:
                num += 1
        return num >= thre

    def binS_LE(isOK, thre):
        ng, ok = 0, 10**9+1
        while abs(ok-ng) > 1:
            mid = (ng+ok) // 2
            if isOK(mid, thre):
                ok = mid
            else:
                ng = mid
        return ok

    def binS_GE(isOK, thre):
        ng, ok = 10**9+1, 0
        while abs(ok-ng) > 1:
            mid = (ng+ok) // 2
            if isOK(mid, thre):
                ok = mid
            else:
                ng = mid
        return ok

    if N % 2:
        num = (N+1)//2
        mn = binS_LE(isOK_LE, num)
        mx = binS_GE(isOK_GE, num)
#        print('mn:', mn, '/ mx:', mx)
#        print(mx-mn)
        return mx-mn+1
    else:
        num = N//2
        mn1 = binS_LE(isOK_LE, num)
        mx1 = binS_GE(isOK_GE, num+1)
        mn2 = binS_LE(isOK_LE, num+1)
        mx2 = binS_GE(isOK_GE, num)
#        print('mn1:', mn1, '/ mx1:', mx1)
#        print('mn2:', mn2, '/ mx2:', mx2)
        mn = mn1+mn2
        mx = mx1+mx2
#        print('mn:', mn, '/ mx:', mx)
#        print(mx-mn)
        return mx-mn+1


ans = solve()
print(ans)
