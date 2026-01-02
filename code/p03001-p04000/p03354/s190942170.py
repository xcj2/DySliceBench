def ge(x):
    return int(x) - 1


(n, m) = tuple(map(int, input().split()))
inp = list(map(ge, input().split()))
arr = [i for i in range(n)]


def root(a):
    global arr
    if arr[a] == a:
        return a
    else:
        tmp = root(arr[a])
        arr[a] = tmp
        return tmp


def sameroot(x, y):
    return root(x) == root(y)


def merge(x, y):
    global arr
    if not sameroot(x, y):
        arr[root(y)] = root(x)


for i in range(m):
    merge(*tuple(map(ge, input().split())))

res = 0
for i in range(n):
    if sameroot(i, inp[i]):
        res += 1
print(res)
