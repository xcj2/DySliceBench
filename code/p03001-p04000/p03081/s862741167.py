def search_right(a, x, lo=0, hi=None, key=lambda x: x):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < key(a[mid]): hi = mid
        else: lo = mid+1
    return lo


def search_left(a, x, lo=0, hi=None, key=lambda x: x):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if key(a[mid]) < x: lo = mid+1
        else: hi = mid
    return lo


def get_fin_pos(s, td, golem_pos):
    for t, d in td:
        if 0 <= golem_pos < len(s) and s[golem_pos] == t:
            golem_pos += 1 if d == "R" else -1
    return golem_pos


n, q = map(int, input().split())
s = "_{}_".format(input())
spells = [input().split() for _ in range(q)]

left = search_right(range(len(s)), 0, key=lambda golem: get_fin_pos(s, spells, golem))
right = search_left(range(len(s)), len(s) - 1, key=lambda golem: get_fin_pos(s, spells, golem))

print(right - left)