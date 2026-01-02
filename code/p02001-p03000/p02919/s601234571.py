def make_tree(n):
    i = 2
    while True:
        if i >= n * 2:
            tree = [-1] * i
            break
        else:
            i *= 2
    return tree

def initialization(tree, a):
    l = len(tree) // 2
    for i in range(l, l + len(a)):
        tree[i] = a[i - l]
    for i in range(l - 1, 0, -1):
        tree[i] = max(tree[2 * i], tree[2 * i + 1])
    return

def update(tree, i, x):
    i += len(tree) // 2
    tree[i] = x
    i //= 2
    while True:
        if i == 0:
            break
        tree[i] = max(tree[2 * i], tree[2 * i + 1])
        i //= 2
    return

def find(tree, s, t):
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
p = list(map(int, input().split()))
q = [0] * n
tree = make_tree(n)
a = [[-1, -1] for _ in range(n)]
b = [[-1, -1] for _ in range(n)]
update(tree, p[0] - 1, 0)
for i in range(1, n):
    a[i][0] = find(tree, p[i], n - 1)
    if not a[i][0] == -1:
        update(tree, p[a[i][0]] - 1, -1)
        a[i][1] = find(tree, p[i], n - 1)
        update(tree, p[a[i][0]] - 1, a[i][0])
    update(tree, p[i] - 1, i)
#print(a)
initialization(tree, [-1] * n)
update(tree, p[-1] - 1, 0)
for i in range(1, n):
    j = n - i - 1
    b[j][0] = find(tree, p[j], n - 1)
    if not b[j][0] == -1:
        update(tree, p[n - b[j][0] - 1] - 1, -1)
        b[j][1] = find(tree, p[j], n - 1)
        update(tree, p[n - b[j][0] - 1] - 1, b[j][0])
    update(tree, p[j] - 1, i)
    if not b[j][0] == -1:
        b[j][0] = n - b[j][0] - 1
    if not b[j][1] == -1:
        b[j][1] = n - b[j][1] - 1
#print(b)
ans = 0
for i in range(n):
    if p[i] == n:
        continue
    if b[i][0] == -1:
        if not a[i][1] == -1:
            x = (n - i) * (a[i][0] - a[i][1])
        elif not a[i][0] == -1:
            x = (n - i) * (a[i][0] + 1)
    elif a[i][0] == -1:
        if not b[i][1] == -1:
            x = (i + 1) * (b[i][1] - b[i][0])
        elif not b[i][0] == -1:
            x = (i + 1) * (n - b[i][0])
    elif a[i][1] == b[i][1] == -1:
        x = (i - a[i][0]) * (n - b[i][0]) + (b[i][0] - i) * (a[i][0] + 1)
    elif b[i][1] == -1:
        x = (b[i][0] - i) * (a[i][0] - a[i][1]) + (i - a[i][0]) * (n - b[i][0])
    elif a[i][1] == -1:
        x = (i - a[i][0]) * (b[i][1] - b[i][0]) + (b[i][0] - i) * (a[i][0] + 1)
    else:
        x = (i - a[i][0]) * (b[i][1] - b[i][0]) + (b[i][0] - i) * (a[i][0] - a[i][1])
    ans += p[i] * x
    #print(ans)
print(ans)