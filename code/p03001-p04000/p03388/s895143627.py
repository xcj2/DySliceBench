def calc_max(a, b, n):
    if n == 0:
        return 0
    m = (b - a) // 2
    if m < 0:
        return a*b
    elif m < n:
        return (a+m)*(b-m)
    else:
        return (a+(n-1))*(b-(n-1))


def judge(a, b, m, x):
    max_value = 0
    if x == 0:
        pass
    elif x < a and x < b:
        max_value = calc_max(1, x, x)
    elif x >= a and x < b:
        max_value = max(calc_max(1, x, a-1),
                        calc_max(a+1, x-(a-1), x-(a-1)))
    else:
        max_value = max(calc_max(1, x+1, x+1-b),
                        calc_max(x + 1-b+1, b-1, a-(x+1-b+1)),
                        calc_max(a+1, x+1-a, x+1-a))
    return True if max_value < m else False


def bs(a, b):
    m = a * b
    lft = 0
    rgt = m
    nxt, prv = -1, -1
    while True:
        nxt = (lft + rgt) // 2
        if nxt == prv:
            return nxt
        if judge(a, b, m, nxt):
            lft = nxt
        else:
            rgt = nxt
        prv = nxt


Q = int(input())
for _ in range(Q):
    A, B = map(int, input().split())
    if A > B:
        A, B = B, A
    print(bs(A, B))
