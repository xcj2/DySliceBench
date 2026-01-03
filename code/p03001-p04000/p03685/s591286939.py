import sys
input = sys.stdin.buffer.readline
R, C, N = map(int, input().split())


class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


def check(x, y):
    if x == 0:
        return y
    elif x == R:
        return R + C + C - y
    elif y == 0:
        return C + R + C + R - x
    elif y == C:
        return C + x
    else:
        return -1


lr_list_raw = []
z_list = []
for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    z1, z2 = check(x1, y1), check(x2, y2)
    if z1 >= 0 and z2 >= 0:
        lr_list_raw.append((min(z1, z2), max(z1, z2)))
        z_list.append(z1)
        z_list.append(z2)

z_list.sort()
idx = {zi: i+1 for i, zi in enumerate(z_list)}
lr_list = []
for l_raw, r_raw in lr_list_raw:
    lr_list.append((idx[l_raw], idx[r_raw]))

'''
print(z_list)
print(idx)
print(lr_list_raw)
'''

bit = Bit(max(idx.values()) + 3)
for l, r in lr_list:
    if (bit.sum(r) - bit.sum(l)) % 2 == 1:
        print('NO')
        exit()
    bit.add(l, 1)
    bit.add(r, 1)

print('YES')
