def make_tree(n):
    i = 2
    while True:
        if i >= n * 2:
            tree1 = [inf] * i
            tree2 = [0] * i
            break
        else:
            i *= 2
    return tree1, tree2

def update(i, x):
    j = len(tree1) // 2 + i
    tree1[j] = x
    j //= 2
    while True:
        if j == 0:
            break
        tree1[j] = min(tree1[2 * j], tree1[2 * j + 1])
        j //= 2
    j = len(tree2) // 2 + i
    tree2[j] = x
    j //= 2
    while True:
        if j == 0:
            break
        tree2[j] = max(tree2[2 * j], tree2[2 * j + 1])
        j //= 2
    return

def find(x, y):
    s = len(tree1) // 2 + x
    t = len(tree1) // 2 + y
    ans1 = inf
    while True:
        if s > t:
            break
        if s % 2 == 0:
            s //= 2
        else:
            ans1 = min(ans1, tree1[s])
            s = (s + 1) // 2
        if t % 2 == 1:
            t //= 2
        else:
            ans1 = min(ans1, tree1[t])
            t = (t - 1) // 2
    s = len(tree2) // 2 + x
    t = len(tree2) // 2 + y
    ans2 = 0
    while True:
        if s > t:
            break
        if s % 2 == 0:
            s //= 2
        else:
            ans2 = max(ans2, tree2[s])
            s = (s + 1) // 2
        if t % 2 == 1:
            t //= 2
        else:
            ans2 = max(ans2, tree2[t])
            t = (t - 1) // 2
    return ans1, ans2

n, k = map(int, input().split())
p = list(map(int, input().split()))
ans = n - k + 1
s = [1] * n
for i in range(1, n):
    if p[i] > p[i - 1]:
        s[i] = s[i - 1] + 1
ans -= max(s.count(k) - 1, 0)
inf = pow(10, 7)
tree1, tree2 = make_tree(n)
for i in range(n):
    update(i, p[i])
for i in range(n - k):
    a, b = find(i, i + k)
    if a == p[i] and b == p[i + k]:
        ans -= 1
print(ans)