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
        tree[i] = max(tree[2 * i], tree[2 * i + 1])
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
            ans = max(ans, tree[s])
            s = (s + 1) // 2
        if t % 2 == 1:
            t //= 2
        else:
            ans = max(ans, tree[t])
            t = (t - 1) // 2
    return ans

n, t = map(int, input().split())
a = list(map(int, input().split()))
tree = make_tree(n)
l = len(tree)
for i in range(n):
    update(i, a[i])
b = [0] * n
for i in range(n - 1):
    b[i] = find(i + 1, n - 1) - a[i]
print(b.count(max(b)))