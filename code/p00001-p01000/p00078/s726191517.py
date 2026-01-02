import sys
f = sys.stdin

def set1(sq):
    x = len(sq) // 2
    y = len(sq) // 2 + 1
    square[y][x] = 1
    return x, y, 1
def mv_r(sq, x, y):
    x = (x + 1) % len(sq)
    y = (y + 1) % len(sq)
    return x, y
def mv_l(sq, x, y):
    x -= 1
    if x < 0:
        x += len(sq)
    y = (y + 1) % len(sq)
    return x, y

def setnext(sq, x, y, i):
    x, y = mv_r(sq, x,y)
    i += 1
    while sq[y][x]:
        x, y = mv_l(sq, x, y)
    sq[y][x] = i
    return x, y, i

while True:
    n = int(f.readline())
    if n == 0:
        break
    square = [[None for j in range(n)] for i in range(n)]
    arg = set1(square)
    for i in range(n * n - 1):
        arg = setnext(square,*arg)

    for line in square:
        for num in line:
            print("{:4d}".format(num),end='')
        print()