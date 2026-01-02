import bisect
sn, tn, qn = map(int, input().split())

LARGE = -100000000
sa = []
ta = []
qa = []
for i in range(sn):
    sa.append(int(input()))
for i in range(tn):
    ta.append(int(input()))
for i in range(qn):
    qa.append(int(input()))

def find_nearest(q, al, s, e):
    idx = bisect.bisect_right(al, q)
    if idx == 0:
        return [al[0], al[0]]
    if idx == len(al):
        return [al[idx - 1], al[idx - 1]]
    return [al[idx - 1], al[idx]]

def move_cost(q, al, bl):
    a1, a2 = find_nearest(q, al, 0, len(al) - 1)
    b1, b2 = find_nearest(q, bl, 0, len(bl) - 1)

    def calc(x1, x2, x3):
        y1 = min(x1, x2)
        y2 = max(x1, x2)
        if x3 >= y1 and x3 <= y2:
            return abs(x1 - x2)
        return abs(x1 - x2) + abs(x2 - x3)
    return min(
        calc(q, a1, b1),
        calc(q, a1, b2),
        calc(q, a2, b1),
        calc(q, a2, b2),
        calc(q, b1, a1),
        calc(q, b1, a2),
        calc(q, b2, a1),
        calc(q, b2, a2),
    )

for q in qa:
    print(move_cost(q, sa, ta))