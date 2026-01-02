# Xは正の整数, pは非負整数, A[k]は偶数
# X == A[k] * (p + 0.5)
# X == A[k]//2 * (2*p + 1)
# X / (A[k]//2) == 2*p + 1
# X % (A[k]//2) == 0 and count_div_two(X) == count_div_two(A[k]//2)

# 全てのcount_div_twoが同じ
# M//最小公倍数 / 2 (切り上げ)

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

# c = 0
# for i in range(1, M+1):
#     print(i, [i/a for a in A])
#     if all(i/a-i//a == 0.5 for a in A):
#         c += 1

# print(c)

def gcd(a, b):
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    return gcd(b%a, a)
def lcm(a, b):
    return (a*b) // gcd(a, b)
def count_div_two(x):
    c = 0
    while x%2 == 0:
        x //= 2
        c += 1
    return c

b = [a//2 for a in A]

if len(set(count_div_two(b_i) for b_i in b)) > 1:
    print(0)
    exit()

b_lcm = 1
for b_i in b:
    b_lcm = lcm(b_lcm, b_i)

c = M//b_lcm
print(-(-c//2))