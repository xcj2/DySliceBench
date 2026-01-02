from collections import defaultdict


def solve2(s):
    ans = 0
    for i, c in enumerate(s):
        if c in '02468':
            ans += i + 1
    return ans


def solve5(s):
    ans = 0
    for i, c in enumerate(s):
        if c in '05':
            ans += i + 1
    return ans


def solve_other(s, p):
    reminders = defaultdict(lambda: 0)
    tmp = 0
    mul = 1
    for c in s[::-1]:
        c = int(c)
        tmp = (tmp + c * mul) % p
        mul = mul * 10 % p
        reminders[tmp] += 1
    reminders[0] += 1
    ans = 0
    for r, cnt in reminders.items():
        ans += cnt * (cnt - 1) // 2
    return ans


n, p = list(map(int, input().split()))
s = input()
if p == 2:
    print(solve2(s))
elif p == 5:
    print(solve5(s))
else:
    print(solve_other(s, p))
