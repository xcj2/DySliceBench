def small(x, y, a):
    a[x][y] += 1
    a[x + 1][y] += 1
    a[x - 1][y] += 1
    a[x][y + 1] += 1
    a[x][y - 1] += 1


def medium(x, y, a):
    small(x, y, a)
    a[x + 1][y + 1] += 1
    a[x - 1][y + 1] += 1
    a[x - 1][y - 1] += 1
    a[x + 1][y - 1] += 1


def large(x, y, a):
    medium(x, y, a)
    a[x + 2][y] += 1
    a[x - 2][y] += 1
    a[x][y + 2] += 1
    a[x][y - 2] += 1


p = [[0] * 13 for i in range(13)]
while 1:
    try:
        x, y, s = map(int, input().split(','))
        if s == 1:
            small(x, y, p)
        elif s == 2:
            medium(x, y, p)
        elif s == 3:
            large(x, y, p)
    except:
        break

w, dens = 0, 0
for i in range(10):
    for j in range(10):
        if p[i][j] == 0:
            w += 1
        if p[i][j] >= dens:
            dens = p[i][j]

print(w)
print(dens)

