N, Q = map(int, input().split())
s = input()
td = [tuple(input().split()) for i in range(Q)]

def left_check(pos):
    nowpos = pos
    for t, d in td:
        if(d=="L" and t==s[nowpos]):
            nowpos -= 1
        elif(d=="R" and t==s[nowpos]):
            nowpos += 1
        if(nowpos == N):
            return False
        elif(nowpos == -1):
            return True
    return False

def right_check(pos):
    nowpos = pos
    for t, d in td:
        if(d=="L" and t==s[nowpos]):
            nowpos -= 1
        elif(d=="R" and t==s[nowpos]):
            nowpos += 1
        if(nowpos == N):
            return False
        elif(nowpos == -1):
            return True
    return True

def nibun(l, h, func):
    low = l
    high = h
    mid = (l+h)//2
    while low <= high:
        x = func(mid)
        if(x):
            low = mid+1
        else:
            high = mid-1
        mid = (low+high)//2
    return mid

print(nibun(0, N-1, right_check)-nibun(0, N-1, left_check))
