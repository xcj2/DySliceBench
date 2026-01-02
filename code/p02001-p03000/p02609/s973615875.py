N = int(input())
X = input()

x_num = int(X, 2)
cnt1 = X.count('1')

p_zero = x_num % (cnt1 + 1)
p_one = (x_num % (cnt1 - 1) if cnt1 - 1 > 0 else 1)


def f(cnt):
    if (cnt > 0):
        pcount = p_count(cnt)
        return f(cnt % pcount) + 1
    else:
        return 0


def p_count(x):
    cnt = 0
    while (x > 0):
        if x % 2 != 0:
            cnt += 1
        x //= 2
    return cnt


def f1(x):
    cnt = 0
    while (x > 0):
        x %= bin(x).count('1')
        cnt += 1
    return cnt


for i, x in enumerate(list(X)):
    if (x == '1'):
        #x_num = int(''.join(X), 2)
        if cnt1 - 1 > 0:
            xxx = (p_one - pow(2, (N - (i + 1)), cnt1 - 1)) % (cnt1 - 1)
            xxx += cnt1 - 1 if xxx < 0 else 0
            print(f(xxx) + 1)
        else:
            print(0)
    else:
        #x_num = int(''.join(X), 2)
        xxx = (p_zero + pow(2, (N - (i + 1)), cnt1 + 1)) % (cnt1 + 1)
        xxx += cnt1 + 1 if xxx < 0 else 0
        print(f(xxx) + 1)