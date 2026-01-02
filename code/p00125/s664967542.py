def isU(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def dd(y,m,d):
    a = 0
    mm = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if isU(y):
        mm[2] = 29

    for i in range(m):
        a += mm[i]
    a += d
    return a

def dy(y1, y2):
    y = 0
    for i in range(y1, y2):
        if isU(i):
            y += 366
        else:
            y += 365
    return y

def get_input():
    while True:
        try:
            yield ''.join(input())
        except EOFError:
            break

while True:
    y1,m1,d1,y2,m2,d2 = [int(i) for i in input().split()]
    if y1 < 0 or m1 < 0 or d1 < 0 or y2 < 0 or m2 < 0 or d2 < 0:
        break
    ans = 0
    ans += dy(y1,y2)
    ans -= dd(y1,m1,d1)
    ans += dd(y2,m2,d2)
    print(ans)

