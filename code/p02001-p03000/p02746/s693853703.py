import sys
def grid(p, level):
    c = 3 ** level
    return ((p[0] % (3 * c)) // c, (p[1] % (3 * c)) // c)

def sub(p1, p2, level):
    # print('sub',(p1, p2, level))
    if level < 0:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    g1, g2 = grid(p1, level), grid(p2, level)
    assert 0 <= g1[0] < 3
    assert 0 <= g1[1] < 3
    assert 0 <= g2[0] < 3
    assert 0 <= g2[1] < 3
    if g1[0] != g2[0]:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    if g1[0] == 1:
        c = 3 ** level
        y1, y2 = p1[1] // c, p2[1] //c
        if abs(y1 - y2) < 2:
            return sub(p1, p2, level - 1)
        i1, i2 = p1[0] % c, p2[0] % c
        xp = min(i1 + i2 + 2, 2 * c - i1 - i2)
        return xp + abs(p1[1] - p2[1])
    return sub(p1, p2, level - 1)

def solve(p1, p2, level):
    g1, g2 = grid(p1, level), grid(p2, level)
    if g1 == g2:
        if level == 0:
           return 0 
        return solve(p1, p2, level - 1)
    if g1[0] == g2[0]:
        return sub(p1, p2, level)
    elif g1[1] == g2[1]:
        return sub((p1[1], p1[0]), (p2[1], p2[0]), level)
    else:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

q = int(input())
for i in range(q):
    a, b, c, d = [int(x) - 1 for x in input().split()]
    print(solve((a, b), (c, d), 30))
