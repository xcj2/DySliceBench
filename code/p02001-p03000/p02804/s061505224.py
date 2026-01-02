import functools
import operator
M = 10**9 + 7
n, k = map(int, input().split())
if k == 1:
    print(0)
    __import__('sys').exit(0)
a = list(map(int, input().split()))
a.sort(reverse=True)

def mul(a, b):
    return mod(a * b)

def powmod(a, n):
    if n == 0:
        return 1
    if n % 2:
        ans = a * powmod(a, n - 1)
    else:
        ans = powmod(a, n // 2) ** 2
    return mod(ans)

def mod(a):
    if a >= M:
        a %= M
    return a
deno = functools.reduce(mul, range(n, n - (k - 1), -1))
nume = functools.reduce(mul, range(1, k))

# max_sum = 0
# min_sum = 0
result = 0
for i, left in enumerate(range(n, k - 1, -1)):
    # print(deno // left * (left - (k - 1)))
    deno = mod(mod(deno * powmod(left, M - 2)) * (left - (k - 1)))
    # print(deno // nume)
    c = mod(deno * powmod(nume, M - 2))

    result += mod(c * a[i]) - mod(c * a[-(i + 1)])
    # max_sum += c * a[i]
    # min_sum += c * a[-(i + 1)]


# print((max_sum - min_sum) % M)
print(result % M)
