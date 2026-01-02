def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def invalid(a, b):
    if a > b:
        a, b = b, a
    return (b % a == 0 and ((b - a) // 2) % a != 0)

def main():
    N, M = map(int, input().split())
    A = list(set(map(int, input().split())))
    A.sort(reverse=True)
    if len(A) == 1:
        l = A[0]
    else:
        if invalid(A[0], A[1]):
            return 0
        l = lcm(A[0], A[1])
        for i in A[2:]:
            if invalid(l, i):
                return 0
            if l % i == 0:
                continue
            if l // 2 > M:
                return 0
            l = lcm(l, i)
    return (M + l // 2) // l

print(main())
