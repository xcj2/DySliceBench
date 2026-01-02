import math
def vec(a, b):
    return [b[0] - a[0], b[1] - a[1]]

def norm(a):
    return math.sqrt(a[0]**2 + a[1]**2)

def cross(a, b):
    return a[0]*b[1] - b[0]*a[1]

def gift_wrap(p_a, p_h, a):
    while True:
        p_h.append(a)
        b = p_a[0]
        for i in range(len(p_a)):
            c = p_a[i]
            if b == a:
                b = c
            else:
                ab = vec(a, b)
                ac = vec(a, c)
                v = cross(ab, ac)
                if v > 0 or (v == 0 and norm(ac) > norm(ab)):
                    b = c
        a = b
        if a == p_h[0]:
            break

while True:
    n = int(input())
    if n == 0:
        break
    p_all = []
    p_hull = []
    for i in range(n):
        p_all.append(list(map(float, input().split(","))))
    p_all = sorted(p_all)
    gift_wrap(p_all, p_hull, p_all[0])
    print(len(p_all) - len(p_hull))

