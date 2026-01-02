import sys


def input():
    return sys.stdin.readline().strip()


def get_sum(x1, x2, y1, y2):
    return acc[x2][y2] - acc[x1][y2] - acc[x2][y1] + acc[x1][y1]


h, w, k = map(int, input().split())
s = [[int(c) for c in input()] for i in range(h)]

acc = [[0 for j in range(w + 1)] for i in range(h + 1)]
for i in range(h):
    for j in range(w):
        acc[i + 1][j + 1] = acc[i][j + 1] + acc[i + 1][j] - acc[i][j] + s[i][j]

ans = h + w

for h_div in range(1 << (h - 1)):
    h_ranges = []
    h_begin = 0
    for i in range(h - 1):
        if h_div >> i & 1:
            h_ranges.append([h_begin, i + 1])
            h_begin = i + 1
    h_ranges.append([h_begin, h])
    div_cnt = len(h_ranges) - 1

    def is_addable():
        for h_range in h_ranges:
            if get_sum(h_range[1], h_range[0], j + 1, w_begin) > k:
                return False
        return True

    w_begin = 0
    for j in range(w):
        if not is_addable():
            w_begin = j
            div_cnt += 1
            if not is_addable():
                div_cnt = h + w
                break
    ans = min(ans, div_cnt)

print(ans)
