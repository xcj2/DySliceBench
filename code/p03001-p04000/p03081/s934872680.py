n, q = map(int, input().split())
s = input()
dic = {}
t_list = []
d_list = []

for i in range(q):
    t, d = input().split()
    t_list.append(t)
    if d == 'L':
        d_list.append(-1)
    else:
        d_list.append(1)


def find_pos(left, right):
    return left + (right - left - 1) // 2


def calc(sites, ts, ds):
    def check(idx):
        num = idx
        for j in range(q):
            site = sites[num]
            if ts[j] == site:
                num += ds[j]
            if num < 0:
                return -1
            if num > n - 1:
                return 1
        return 0

    def func(left, right):
        assert left > -1
        assert right < n + 1
        if right - left == 1:
            if check(left) > -1:
                return left
            else:
                return right
        pos = find_pos(left, right)
        if check(pos) > -1:
            return func(left, pos + 1)
        else:
            return func(pos + 1, right)
    return func


f1 = calc(s, t_list, d_list)
f2 = calc(s[::-1], t_list, [-i*1 for i in d_list])
print(n - f1(0, n) - f2(0, n))