import bisect

def make_tree(n):
    i = 2
    while True:
        if i >= n * 2:
            tree = [0] * i
            break
        else:
            i *= 2
    return tree

def update(i, x):
    i += len(tree) // 2
    tree[i] = x
    i //= 2
    while True:
        if i == 0:
            break
        tree[i] = tree[2 * i] + tree[2 * i + 1]
        i //= 2
    return

def find(s, t):
    s += len(tree) // 2
    t += len(tree) // 2
    ans = 0
    while True:
        if s > t:
            break
        if s % 2 == 0:
            s //= 2
        else:
            ans += tree[s]
            s = (s + 1) // 2
        if t % 2 == 1:
            t //= 2
        else:
            ans += tree[t]
            t = (t - 1) // 2
    return ans

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
s = [0] * (n + 1)
for i in range(n):
    s[i + 1] += s[i] + a[i]
for i in range(n + 1):
    s[i] -= k * i
d = dict()
for i in s:
    if not i in d:
        d[i] = 1
    else:
        d[i] += 1
x = list(d.keys())
x.sort()
tree = make_tree(len(x))
for i in range(len(x)):
    update(i, d[x[i]])
cnt = 0
l = len(tree) // 2
for i in s:
    b = bisect.bisect_left(x, i)
    update(b, tree[l + b] - 1)
    cnt += find(b, l - 1)
print(cnt)