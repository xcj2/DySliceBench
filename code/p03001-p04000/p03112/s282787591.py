A, B, Q = map(int, input().split())
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]
x = [int(input()) for _ in range(Q)]


def bsearch(n, arr):
    l = 0
    r = len(arr)
    m = (l + r) // 2
    while l != m:
        if n <= arr[m]:
            r = m
        else:
            l = m
        m = (l + r) // 2
    if r < len(arr) and abs(arr[l] - n) > abs(arr[r] - n):
        return r
    else:
        return l


def bsearch_l(n, arr):
    l = 0
    r = len(arr)
    m = (l + r) // 2
    while l != m:
        if n <= arr[m]:
            r = m
        else:
            l = m
        m = (l + r) // 2
    return l


def calc_distance(x, l, c, near_idx):
    ret = abs(x - l)
    if c == 's':
        next_l = t[near_idx]
    else:
        next_l = s[near_idx]
    ret += abs(next_l - l)
    return ret


st = []
for i, s_i in enumerate(s):
    t_i = bsearch(s_i, t)
    st.append((s_i, 's', t_i))

for i, t_i in enumerate(t):
    s_i = bsearch(t_i, s)
    st.append((t_i, 't', s_i))

st = sorted(st)
starr = sorted(s + t)

ans_list = []
for i, x_i in enumerate(x):
    st_i = bsearch_l(x_i, starr)
    l, c, near_idx = st[st_i]
    ans = calc_distance(x_i, l, c, near_idx)
    if st_i < len(st) - 1:
        l, c, near_idx = st[st_i + 1]
        ans = min(ans, calc_distance(x_i, l, c, near_idx))
    ans_list.append(ans)

for i, ans in enumerate(ans_list):
    print(ans)