def f(i, y, S):
    while i < y:
        if S[i + 2] == '.':
            i += 2
        elif S[i + 1] == '.':
            i += 1
        else:
            return False
    return True
def g(i, y, S):
    while i < y:
        if S[i + 2] == '.':
            i += 2
        elif S[i + 1] == '.':
            i += 1
        else:
            break
    return i
def dc(n, a, b, c, d, S):
    S = list(S)
    S[b] = 'B'
    while a < b:
        a = g(a, c, S)
        if b == d:
            return a >= c
        elif S[b + 1] == '.':
            S[b] = '.'
            b += 1
            S[b] = 'B'
        elif S[b + 2] == '.':
            S[b] = '.'
            b += 2
            S[b] = 'B'
        else:
            return a >= c
    return True
def solve():
    n, a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    S = input() + "##"
    if c < d:
        S = list(S)
        return f(b, d, S) and f(a, c, S)
    else:
        return dc(n, a, b, c, d, S)
    return True
print("Yes" if solve() else "No")
