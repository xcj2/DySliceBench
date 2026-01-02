def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))

h,w,n = getList()
sy, sx = getList()
taka = input()
aoki = input()

def game(taka, aoki, mt, ma, buf, bmax):
    for ta, ao in zip(taka, aoki):
        if ta == mt:
            buf -= 1
            if buf == 0:
                return False
        if ao == ma:
            buf = min(buf + 1, bmax)

    return True

ga = game(taka,aoki,"U", "D", sy, h)
gb = game(taka,aoki,"D", "U", h - sy + 1, h)
gc = game(taka,aoki,"L", "R", sx, w)
gd = game(taka,aoki,"R", "L", w - sx + 1, w)

if ga and gb and gc and gd:
    print("YES")

else:
    print("NO")