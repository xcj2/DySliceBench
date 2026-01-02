N=int(input())
ab = [tuple(map(int, input().split())) for i in range(N)]
a,b = zip(*ab)
res = 0
ma = max(b)+1

def solve_left(idx):
    left = sum([1 for l,r in ab if idx<l])
    if left > N//2:
        return False
    return True

def solve_right(idx):
    right = sum([1 for l,r in ab if idx>r])
    if right > N//2:
        return False
    return True
def solve_left2(idx):
    left = sum([1 for l,r in ab if idx<l])
    if left > N//2-1:
        return False
    return True

def solve_right2(idx):
    right = sum([1 for l,r in ab if idx>r])
    if right > N//2-1:
        return False
    return True

ok = ma
ng = 0
while abs(ok-ng) > 1:
    cnt = (ok + ng) // 2
    if solve_left(cnt):
        ok = cnt
    else:
        ng = cnt
res_left = ok

ok = 0
ng = ma
while abs(ok-ng) > 1:
    cnt = (ok + ng) // 2
    if solve_right(cnt):
        ok = cnt
    else:
        ng = cnt
res_right = ok

if N%2==0:
    ok = ma
    ng = 0
    while abs(ok - ng) > 1:
        cnt = (ok + ng) // 2
        if solve_left2(cnt):
            ok = cnt
        else:
            ng = cnt
    res_left2 = ok
    
    ok = 0
    ng = ma
    while abs(ok - ng) > 1:
        cnt = (ok + ng) // 2
        if solve_right2(cnt):
            ok = cnt
        else:
            ng = cnt
    res_right2 = ok

if N%2==1:
    res = (res_right-res_left) + 1
else:
    # print((res_left,res_left2),(res_right,res_right2))
    res = (res_right+res_right2)-(res_left+res_left2) + 1
print(res)