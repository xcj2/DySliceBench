import sys

def left(x, y, z):
    return x**2 + y**2 + z**2 + x*y + y*z + z*x

def count(x, y, z):
    uniq_num = len(set([x, y, z]))
    if uniq_num == 3:
        return 6  # 3!
    elif uniq_num == 2:
        return 3  # 3C1
    else:
        return 1

def show_result(ans):
    for n,fn in enumerate(ans[1:]):
        print(fn)

N = int(input())

ans = [0]*(N+1)
x = y = z = 1
while x <= N-3 and left(x, y, z) <= N:
    while y <= N-3 and left(x, y, z) <= N:
        while z <= N-3 and left(x, y, z) <= N:
            l = left(x, y, z)
            ans[l] += count(x, y, z)
            z += 1
        y += 1
        z = y
    x += 1
    y = z = x
show_result(ans)