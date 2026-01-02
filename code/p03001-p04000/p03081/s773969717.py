n, q = [int(i) for i in input().split(" ")]
s = input()
qs = [[]] * q

for i in range(0, q):
    qs[i] = input().split(" ")

def dest(i):
    global s
    global n
    global qs
    cur = i
    for qsi in qs:
        if s[cur] == qsi[0]:
            if qsi[1] == "R":
                cur += 1
                if cur >= n:
                    return cur
            else:
                cur -= 1
                if cur < 0:
                    return cur
    return cur

def sL(l, r):
    if l == r:
        return l
    h = (l + r) // 2
    if dest(h) < 0:
        return sL(h + 1, r)
    else:
        return sL(l, h)
    
def sR(l, r):
    global n
    if l == r:
        return l
    h = (l + r) // 2
    if dest(h) < n:
        return sR(h + 1, r)
    else:
        return sR(l, h)
    
print(sR(0, n) - sL(0, n))