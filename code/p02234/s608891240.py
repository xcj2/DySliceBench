n = int(input())


def memorizer(f):
    memo = [ [None] * n for _ in range(n) ]
    for i in range(n):
        memo[i][i] = 0

    def inner_memo(a, b):
        if memo[a][b] is not None:
            return memo[a][b]
        rslt = memo[a][b] = f(a, b)
        return rslt

    return inner_memo

@memorizer
def minimum(a, b):
    return min(minimum(a, i) + minimum(i + 1, b) + l[a] * l[i + 1] * l[b + 1] for i in range(a, b))



a, b = map(int, input().split())

l = []
l.append(a)
l.append(b)

n1 = n - 1

while n1 != 0:
    a, b = map(int, input().split())
    l.append(b)
    n1 -= 1

print(minimum(0, n - 1))


