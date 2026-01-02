def comb(a, b):
    if (a < b) or (a < 0) or (b < 0):
        return 0
    res = 1
    for i in range(b):
        res *= a - i
        res //= i + 1
    return res

def solve(n, k):
    s = str(n)
    d = len(s)
    def f(i, t, ok):
        if ok:
            return comb(d-i, t) * (9**t)
        elif t == 0:
            return 1
        elif i == d:
            return 0
        if s[i] == "0":
            return f(i+1, t, False)
        res = f(i+1, t, True)
        if t > 0:
            for j in range(1, 10):
                if int(s[i]) > j:
                    res += f(i+1, t-1, True)
                elif int(s[i]) == j:
                    res += f(i+1, t-1, False)
                else:
                    break
        return res
    return f(0, k, False)

n = int(input())
k = int(input())
print(solve(n, k))