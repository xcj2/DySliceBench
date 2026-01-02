def Is_honest(x, honest, n):
    for i in range(n):
        honest[i] = (x%2 == 1)
        x //= 2


def checker(honest, da, n):
    for i in range(n):
        if honest[i]:
            size = len(da[i])
            for j in range(size):
                ok = (da[i][j][1] == 1)
                if honest[da[i][j][0]]^ok:
                    return False
    return True

def counter(honest):
    ret = 0
    for i in honest:
        if i:
            ret += 1
    return ret

n = int(input())
da = [[] for i in range(n)]
for i in range(n):
    a = int(input())
    for j in range(a):
        da[i].append(list(map(int,input().split())))
        da[i][-1][0] -= 1

ans = 0
honest = [False for i in range(n)]
m = 2 ** n

for i in range(m):
    Is_honest(i, honest, n)
    if checker(honest, da, n):
        ans = max(ans, counter(honest))

print(ans)