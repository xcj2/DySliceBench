height, width, k = map(int, input().split())

start_w = 1
end_w = width

if end_w <= 1:
    print(1)
    exit()


def enum_no_relation_cases(n, m=0):
    front = n - (start_w + 1) - (m * (m - 1)) // 2
    rear = end_w - (n + 1) - (m * (m + 1)) // 2
    return int(enum_amida_all_cases(front) * enum_amida_all_cases(rear))


def enum_amida_all_cases(n):
    if n < 1:
        return 1
    return fibonacci(n + 2)


f = [1, 1, 1] + ([0] * (end_w - 1))


def fibonacci(n):
    if f[n] == 0:
        f[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return f[n]


ans = [[0] * (1 + end_w + 1) for i in range(height + 1)]
ans[0][start_w] = 1
search_range = start_w + 1
for h in range(1, height + 1):
    for w in range(1, search_range + 1):
        from_just_above = ans[h - 1][w] * enum_no_relation_cases(w)
        from_upper_left = ans[h - 1][w - 1] * enum_no_relation_cases(w, -1)
        from_upper_right = ans[h - 1][w + 1] * enum_no_relation_cases(w, 1)
        ans[h][w] = from_just_above + from_upper_left + from_upper_right

    if search_range < end_w:
        search_range += 1

print(ans[height][k] % 1000000007)