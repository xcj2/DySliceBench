n, m = map(int, input().split())
sc = [list(map(int, input().split())) for i in range(m)]
sorted(sc)

def f1():
    if m == 0:
        return 0
    for i in range(1, m):
        if sc[i - 1][0] == sc[i][0] and sc[i - 1][1] != sc[i][1]:
            return -1
    return sc[0][1]

def f2():
    if m == 0:
        return 10
    for i in range(1, m):
        if sc[i - 1][0] == sc[i][0] and sc[i - 1][1] != sc[i][1]:
            return -1
    l = [10 * i + j for i in range(1, 10) for j in range(0, 10)]
    sl = ["1", "0"]
    for i in range(m):
        sl[sc[i][0] - 1] = str(sc[i][1])
    s = sl[0] + sl[1]
    for i in l:
        if str(i) == s:
            return i
    return -1

def f3():
    if m == 0:
        return 100
    for i in range(1, m):
        if sc[i - 1][0] == sc[i][0] and sc[i - 1][1] != sc[i][1]:
            return -1
    l = [100 * i + 10 * j + k for i in range(1, 10) for j in range(0, 10) for k in range(0, 10)]
    sl = ["1", "0", "0"]
    for i in range(m):
        sl[sc[i][0] - 1] = str(sc[i][1])
    s = sl[0] + sl[1] + sl[2]
    for i in l:
        if str(i) == s:
            return i
    return -1

if n == 1:
    print(f1())
elif n == 2:
    print(f2())
else:
    print(f3())
