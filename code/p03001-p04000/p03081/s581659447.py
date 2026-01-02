N,Q = map(int,input().split())
s = input()
info = [input().split() for _ in range(Q)]

def biserch(ok,ng,judge):
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if judge(mid):
            ok = mid
        else:
            ng = mid
    return ok

def left_out(i):
    now = i
    for t, d in info:
        if s[now] == t:
            if d == "L":
                now -= 1
            elif d == "R":
                now += 1
        if now < 0:
            return True
        elif now > N-1:
            return False
    return False

def right_out(i):
    now = i
    for t, d in info:
        if s[now] == t:
            if d == "L":
                now -= 1
            elif d == "R":
                now += 1
        if now > N-1:
            return True
        elif now < 0:
            return False
    return False

left = biserch(ok=-1,ng=N,judge=left_out)
right = biserch(ok=N,ng=-1,judge=right_out)
ans = right - (left + 1)
print(ans)