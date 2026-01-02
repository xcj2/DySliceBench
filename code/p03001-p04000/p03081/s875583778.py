N, Q = map(int, input().split())
s = list(input())
t = [input().split() for _ in range(Q)]


def func(n):
    pos = n
    for x in t:
        if x[0] == s[pos]:
            if x[1] == 'L':
                pos -= 1
                if pos < 0:
                    return 'L'
            else:
                pos += 1
                if pos == N:
                    return 'R'
    return 'T'


def calcl(pl, pr):
    if pl == pr:
        return pl
    else:
        p = (pr + pl) // 2
        a = func(p)
        if a == 'T':
            return calcl(pl, p)
        else:
            return calcl(p+1, pr)


def calcr(pl, pr):
    if pl == pr:
        return pl
    else:
        p = (pr + pl + 1) // 2
        a = func(p)
        if a == 'T':
            return calcr(p, pr)
        else:
            return calcr(pl, p - 1)


pl = 0
pr = N - 1
p = (pl + pr) // 2
a = func(p)
ans = 0
if a == 'T':
    p1 = calcl(pl, p)
    p2 = calcr(p, pr)
    ans = p2 - p1 + 1
elif a == 'L':
    while True:
        pl = p + 1
        if pl == N:
            break
        p = (pl + pr) // 2
        a = func(p)
        if a == 'T':
            p1 = calcl(pl, p)
            p2 = calcl(p, pr)
            ans = p2 - p1 + 1
            break
elif a == 'R':
    while True:
        pr = p - 1
        if pr == -1:
            break
        p = (pl + pr) // 2
        a = func(p)
        if a == 'T':
            p1 = calcl(pl, p)
            p2 = calcl(p, pr)
            ans = p2 - p1 + 1
            break
print(ans)