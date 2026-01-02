import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

x,k,d = map(int,readline().split())

x = abs(x)

#連続な二分探索
def func(mid): #ここが関数部分
    if x-d*mid < 0:
        return True
    else:
        return False

def binary_search(): #2分探索
    ok = 10**18
    ng = -1
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if func(mid):
            ok = mid
        else:
            ng = mid

    if abs(x-d*ok) <= abs(x-d*ng):
        return ok
    else:
        return ng

if x-k*d >= 0:
    print(x-k*d)
else:
    times = binary_search()
    ans = abs(x-d*times)
    if even(k-times):
        print(ans)
    else:
        print(min(abs(ans+d),abs(ans-d)))
