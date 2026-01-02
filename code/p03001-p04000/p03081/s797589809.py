N,Q = map(int,input().split())
s = input()
info = [input().split() for _ in range(Q)]

def left_out():
    left = -1; right = N
    while right - left > 1:
        mid = (left+right) // 2
        if judge(mid) == -1:
            left = mid
        else:
            right = mid
    return left

def right_out():
    left = -1; right = N
    while right - left > 1:
        mid = (left+right) // 2
        if judge(mid) == 1:
            right = mid
        else:
            left = mid
    return right

def judge(i):
    now = i
    for t, d in info:
        if s[now] == t:
            if d == "L":
                now -= 1
            elif d == "R":
                now += 1
        if now < 0:
            return -1
        elif N <= now:
            return 1
    return 0
    
left = left_out()
right = right_out()
ans = right - left - 1
print(ans)