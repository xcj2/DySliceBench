n = int(input())
m = []


def memoize(f):
    memo = [[None] * n for _ in range(n)]
    for i in range(n):
        memo[i][i] = 0

    def main(b, e):
        if memo[b][e] is not None:
            return memo[b][e]
        result = memo[b][e] = f(b, e)
        return result

    return main


@memoize
def contract(b, e):
    return min(contract(b, i) + contract(i + 1, e) + m[b] * m[i + 1] * m[e + 1] for i in range(b, e))


r, c = map(int, input().split())
m.append(r)
m.append(c)
nc = n - 1
while nc:
    r, c = map(int, input().split())
    m.append(c)
    nc -= 1

print(contract(0, n - 1))