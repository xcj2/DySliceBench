n = int(input())
aaa = list(map(int, input().split()))
bbb = list(map(int, input().split()))
ccc = list(map(int, input().split()))

aaa.sort()
ccc.sort()

def is_ok_a(mid, b):
    if mid < 0:
        return True
    elif mid >= n:
        return False
    else:
        return aaa[mid] < b

def m_bisect_a(ng, ok, b):
    while abs(ng - ok) > 1:
        mid = (ng + ok) // 2
        if is_ok_a(mid, b):
            ok = mid
        else:
            ng = mid
    return ok

def is_ok_c(mid, b):
    if mid < 0:
        return False
    elif mid >= n:
        return True
    else:
        return ccc[mid] > b

def m_bisect_c(ng, ok, b):
    while abs(ng - ok) > 1:
        mid = (ng + ok) // 2
        if is_ok_c(mid, b):
            ok = mid
        else:
            ng = mid
    return ok

ans = 0
for i in range(n):
    b = bbb[i]
    ng, ok = n, -1
    cnt_a = m_bisect_a(ng, ok, b) + 1
    ng, ok = -1, n
    cnt_c = n - m_bisect_c(ng, ok, b)
    ans += (cnt_a * cnt_c)

print(ans)