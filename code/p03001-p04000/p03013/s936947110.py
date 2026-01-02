mod = 1000000007

def add(a, b):
    return (a + b) % mod

def sub(a, b):
    return (a + mod - b) % mod

def mul(a, b):
    return ((a % mod) * (b % mod)) % mod
    
a = []
N, M = map(int, input().split())
for i in range(M):
    a.append(int(input()))

results = []

flag = True

for m in range(1, M):
    if a[m] - a[m - 1] == 1:
        flag = False
        break

flag_end = True
if M == 0:
    flag_end = False

def Fib(n):
    a, b = 0, 1
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(n-2):
            a, b = b, a + b
        return b

if flag and flag_end:
    for m in range(M):
        if m == 0:
            results.append(Fib(a[m] + 1))
        else:
            results.append(Fib(a[m] - a[m - 1]))
    results.append(Fib(N - a[m] + 1))
    result = 1
    for i in range(len(results)):
        result = mul(result, results[i])
    print(result % mod)
elif not flag:
    print(0)
else:
    print(Fib(N + 2) % mod)













