def make_tree(n):
    i = 2
    while True:
        if i >= n * 2:
            tree = [[inf] * i for _ in range(26)]
            break
        else:
            i *= 2
    return tree

def update(i, x, tree):
    i += len(tree) // 2
    tree[i] = x
    i //= 2
    while True:
        if i == 0:
            break
        tree[i] = min(tree[2 * i], tree[2 * i + 1])
        i //= 2
    return

def find(s, t, tree):
    s += len(tree) // 2
    t += len(tree) // 2
    ans = inf
    while True:
        if s > t:
            break
        if s % 2 == 0:
            s //= 2
        else:
            ans = min(ans, tree[s])
            s = (s + 1) // 2
        if t % 2 == 1:
            t //= 2
        else:
            ans = min(ans, tree[t])
            t = (t - 1) // 2
    return ans

s = list(input())
t = list(input())
inf = 10 ** 6
n = len(s)
first = [-2] * 26
tree = make_tree(n)
for i in range(n):
    m = ord(s[i]) - 97
    update(i, i, tree[m])
    if first[m] == -2:
        first[m] = i
ans = 1
c = -1
for i in t:
    m = ord(i) - 97
    if not c == -1:
        u = -1
        u = find(c + 1, n - 1, tree[m])
        if u == -1 or u == inf:
            ans += n
            c = -1
        else:
            c = u
    if c == -1:
        c = first[m]
        if c == -2:
            print(-1)
            exit()
ans += c
print(ans)