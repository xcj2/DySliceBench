def runlen(a):
    n = len(a)
    result = []
    count = 1
    for i in range(n):
        if i == n - 1 or a[i] != a[i + 1]:
            result.append((count, a[i]))
            count = 1
        else:
            count += 1
    return result

def f(s):
    rl = runlen(s)
    result = ""
    for (count, c) in rl:
        result += str(count)
        result += c
    return result

def apply(f, n, x):
    for _ in range(n):
        x = f(x)
    return x

while True:
    n = int(input())
    if n == 0:
        break
    s = input().strip()
    print(apply(f, n, s))
