height, width, k = map(int, input().split())

ans = [[0] * (width + 2) for i in range(height + 1)]
start_w = 1
end_w = width
start_h = 0
ans[start_h][start_w] = 1
search_range = start_w + 1 if end_w > 1 else 1
f = [0] * (width + 2)
f[0], f[1], f[2] = 1, 1, 1


def det_unused(n, m=0):
    front = n - (start_w + 1)
    rear = end_w - (n + 1)

    if m == -1:
        front -= 1
    elif m == 1:
        rear -= 1

    ret = int(calc(front) * calc(rear))
    return ret


def calc(n):
    if n < 1:
        return 1
    return calc_f(n+2)


def calc_f(n):
    if f[n] == 0:
        f[n] = calc_f(n - 1) + calc_f(n - 2)
    return f[n]


for h in range(1, height + 1):
    for w in range(1, search_range + 1):
        prev_ans = ans[h - 1]
        ans[h][w] = prev_ans[w] * det_unused(w) + prev_ans[w - 1] * det_unused(w, -1) + prev_ans[w + 1] * det_unused(w, 1)
        ans[h][w] %= 1000000007
    if search_range < end_w:
        search_range += 1

print(ans[height][k])