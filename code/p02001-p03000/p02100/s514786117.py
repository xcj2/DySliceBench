def parse(S):
    poly = []
    t = []
    for x in S.split('+'):
        if '-' in x:
            t = t + ['-' + a if i != 0 else a for i, a in enumerate(x.split('-'))]
        else:
            t.append(x)

    for x in t:
        if '^' in x:
            t = x.split('x^')
            if len(t[0]) == 0:
                a = 1
            else:
                a = int(t[0])
            b = int(t[1])
        else:
            if 'x' in x:
                if x == 'x':
                    a = 1
                elif x == '-x':
                    a = -1
                else:
                    a = int(x[:-1])
                b = 1
            else:
                a = int(x)
                b = 0

        poly.append((a, b))

    return poly

def calc_yaku(n):
    ret = []
    for i in range(n + 1):
        if i != 0 and n % i == 0:
            ret.append(i)

    return reversed(sorted(ret + [-x for x in ret]))

def calc(poly, x):
    ret = 0
    for p in poly:
        ret += p[0] * x ** p[1]

    return ret


def solve(S):
    poly = parse(S)
    n = abs(poly[-1][0])
    yaku = calc_yaku(n)

    ans = []
    for x in yaku:
        if calc(poly, x) == 0:
            ans.append(-x)

    for x in ans:
        if x > 0:
            print('(x+{})'.format(x), end='')
        else:
            print('(x{})'.format(x), end='')

    print('')

S=input()
solve(S)