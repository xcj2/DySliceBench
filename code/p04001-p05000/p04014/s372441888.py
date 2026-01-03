import math

def digitsum(x, b):
    accum = 0
    while x > 0:
        accum += x % b
        x //= b
    return accum

def solve(n, s, max_ns):
    if n < s: return -1
    # 1 <= n < 2**37
    max_digits = int(math.ceil(math.log2(max_ns)))
    # sentinel.
    min_b = n + 2

    # 1桁
    if n == s:
         min_b = n + 1

    # 2桁
    # 10*11程度調べるのは重すぎる
    # それぞれの数字0<=x,y<=b-1として
    # xb + y = n, x + y = s
    # => x(b-1) = n-s
    # 2 .. (n-s)^(1/2) の範囲で約数qを持てば、b=q+1またはb=(n-s)//q+1が候補
    for q in range(1, int((n - s)**0.5) + 1):
        if (n - s) % q == 0:
            for b in [q + 1, (n - s) // q + 1]:
                if b < min_b:
                    if digitsum(n, b) == s:
                        min_b = b

    # 3桁以上
    # <=> n >= b**(3 - 1)
    # <=> b <= n**(1/2)
    b_low = 2
    b_high = min(min_b, int(n ** 0.5) + 1)
    for b in range(b_low, b_high):
        if digitsum(n, b) == s:
            min_b = b

    if min_b < n + 2:
        return min_b
    return -1

def test():
    import random
    random.seed(0)
    for i in range(100):
        b = random.randint(2, 10**11)
        n = random.randint(1, 10**11)
        s = digitsum(n, b)
        solved_b = solve(n, s, 10**11)
        if s == digitsum(n, solved_b) and solved_b <= b:
            print('OK b={}, n={}, s={}, solved_b={}'.format(b, n, s, solved_b))
        else:
            print('NG!!! b={}, n={}, s={}, solved_b={}'.format(b, n, s, solved_b))

if __name__ == '__main__':
    n = int(input())
    s = int(input())
    print(solve(n, s, 10**11))
