def make_tree(n):
    i = 2
    while True:
        if i >= n * 2:
            tree = [-1] * i
            break
        else:
            i *= 2
    return tree

def initialization(a):
    l = len(tree) // 2
    for i in range(l, l + len(a)):
        tree[i] = a[i - l]
    for i in range(l - 1, 0, -1):
        tree[i] = max(tree[2 * i], tree[2 * i + 1])
    return

def update(i, x):
    i += len(tree) // 2
    tree[i] = x
    i //= 2
    while True:
        if i == 0:
            break
        tree[i] = max(tree[2 * i], tree[2 * i + 1])
        i //= 2
    return

def find(s, t):
    s += len(tree) // 2
    t += len(tree) // 2
    ans = -1
    while True:
        if s > t:
            break
        if s % 2 == 0:
            s //= 2
        else:
            ans = max(ans, tree[s])
            s = (s + 1) // 2
        if t % 2 == 1:
            t //= 2
        else:
            ans = max(ans, tree[t])
            t = (t - 1) // 2
    return ans

n = int(input())
a = list(map(int, input().split()))
x1, x2 = [0] * n, [0] * n
tree = make_tree(n)
for i in range(n):
    update(a[i] - 1, i)
    x1[i] = find(0, a[i] - 2)
initialization([-1] * n)
for i in range(n):
    j = n - i - 1
    update(a[j] - 1, i)
    x2[j] = n - find(0, a[j] - 2) - 1
ans = 0
for i in range(n):
    ans += a[i] * (i - x1[i]) * (x2[i] - i)
print(ans)