import sys

inf = 1<<30

def solve():
    n = int(sys.stdin.readline().rstrip())

    for i in range(n):
        x, y = sys.stdin.readline().split()

        x = mcxi_to_digit(x)
        y = mcxi_to_digit(y)

        ans = digit_to_mcxi(x + y)

        print(ans)

def mcxi_to_digit(x):
    res = 0
    ps = -1

    for i, num in enumerate(x):
        if ps == i:
            continue
        if num.isdigit():
            if x[i + 1] == 'm':
                res += 1000 * int(num)
            elif x[i + 1] == 'c':
                res += 100 * int(num)
            elif x[i + 1] == 'x':
                res += 10 * int(num)
            else:
                res += int(num)

            ps = i + 1
        else:
            if num == 'm':
                res += 1000
            elif num == 'c':
                res += 100
            elif num == 'x':
                res += 10
            else:
                res += 1

    return res

def digit_to_mcxi(x):
    res = []

    if x % 10 == 1:
        res.append('i')
    elif x % 10 > 1:
        res.append('i')
        res.append(str(x % 10))

    x //= 10

    if x % 10 == 1:
        res.append('x')
    elif x % 10 > 1:
        res.append('x')
        res.append(str(x % 10))

    x //= 10

    if x % 10 == 1:
        res.append('c')
    elif x % 10 > 1:
        res.append('c')
        res.append(str(x % 10))

    x //= 10

    if x % 10 == 1:
        res.append('m')
    elif x % 10 > 1:
        res.append('m')
        res.append(str(x % 10))

    res.reverse()

    return ''.join(res)

if __name__ == '__main__':
    solve()