def rotate_matriz(s, x, y):
    ex = [[""] * x for _ in range(y)]
    for i in range(x):
        for j in range(y):
            ex[j][i] = s[i][j]
    return ex


def pprint(s, n):
    for i in range(n):
        print("".join(s[i]))


def check(s, n):
    ex = []
    ct = 0
    for i in range(n):
        if "#" in s[i]:
            ex.append(s[i][:])
        else:
            ct += 1
    return ex, n - ct


h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
b, h = check(a, h)
b = rotate_matriz(b, h, w)
b, w = check(b, w)
b = rotate_matriz(b, w, h)
pprint(b, h)
