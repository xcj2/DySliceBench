def checkW(H, W, a):
    if W % 3 == 0:
        return 0
    x = int(W / 3) + a
    y = int(H / 2)
    if x == 0 or y == 0 or (W-x) == 0:
        return 10000000000
    S = [x*H, (W-x)*y, (W-x)*(H-y)]
    #print(x, y, S, max(S),min(S))
    return max(S) - min(S)

def checkH(H, W, a):
    if H % 3 == 0:
        return 0
    x = int(W / 2)
    y = int(H / 3) + a
    if x == 0 or y == 0 or (H-y) == 0:
        return 10000000000
    S = [W*y, x*(H-y), (W-x)*(H-y)]
    #print(x, y, S, max(S),min(S))
    return max(S) - min(S)

def check(H,W):
    x = int(W/3)
    x2 = int((W-x)/2)
    x3 = int(W-x-x2)
    S = [x*H, x2*H, x3*H]
    mx = max(S) - min(S)
    y = int(H/3)
    y2 = int((H-y)/2)
    y3 = int(H-y-y2)
    S = [W*y, W*y2, W*y3]
    my = max(S) - min(S)
    return min(mx, my)

s = input().split(' ')
H = int(s[0])
W = int(s[1])
print(min(checkW(H,W,0), checkW(H,W,1),
          checkH(H,W,0), checkH(H,W,1),
          check(H,W)))