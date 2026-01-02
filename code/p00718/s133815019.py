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

    mcxi = {'m':1000, 'c':100, 'x':10, 'i':1}

    for i, num in enumerate(x):
        if ps == i:
            continue
        if num.isdigit():
            res += mcxi[x[i + 1]] * int(num)
            ps = i + 1
        else:
            res += mcxi[num]

    return res

def digit_to_mcxi(x):
    res = []
    mcxi = ['i', 'x', 'c', 'm']

    for k in range(len(mcxi)):
        if x % 10 >= 1:
            res.append(mcxi[k])

            if x % 10 > 1:
                res.append(str(x % 10))

        x //= 10
        
    res.reverse()

    return ''.join(res)

if __name__ == '__main__':
    solve()