import itertools
def f(a, b):
    return max(len(str(a)), len(str(b)))
def p(n):
    l = []
    a, b = 0, 2
    while b * b <= n:
        if n % b == 0:
            n //= b
            l += [b]
        else:
            b += 1 + a
            a = 1
    if n > 1 : l += [n]
    return l

def main():
    N = int(input())
    l = p(N)
    if len(l) < 2:
        print(f(N, 1))
    else:
        w = len(l)
        ans = len(str(N))
        for i in itertools.product([0, 1], repeat=w):
            a = b = 1
            for j in range(w):
                if i[j] == 0:
                    a *= l[j]
                else:
                    b *= l[j]
            ans = min(ans, f(a, b))
        print(ans)
if __name__ == '__main__':
    main()
