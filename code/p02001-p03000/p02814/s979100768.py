def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def judge(A):
    B = [0] * len(A)
    for i, a in enumerate(A):
        b = 0
        while a % 2 == 0:
            b += 1
            a //= 2
        B[i] = b
    if len(set(B)) == 1:
        return True
    else:
        return False


N, M = map(int, input().split())
A = [int(i) // 2 for i in input().split()]
A = list(set(A))
m = A[0]

if judge(A):
    for a in A[1:]:
        m = lcm(m, a)

    M //= m
    ans = (M + 1) // 2
else:
    ans = 0
print(ans)
