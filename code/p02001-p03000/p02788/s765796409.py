import math

def make_tree(n):
    i = 2
    while True:
        if i >= n * 2:
            tree = [0] * i
            break
        else:
            i *= 2
    return tree

def get(i):
    i += len(tree) // 2
    ans = 0
    while True:
        if i == 0:
            break
        ans += tree[i] 
        i //= 2
    return ans

def update(s, t, x):
    s += len(tree) // 2
    t += len(tree) // 2
    while True:
        if s > t:
            break
        if s % 2 == 0:
            s //= 2
        else:
            tree[s] += x
            s = (s + 1) // 2
        if t % 2 == 1:
            t //= 2
        else:
            tree[t] += x
            t = (t - 1) // 2
    return

n, d, a = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
s.sort()
tree = make_tree(n)
l = len(tree)
for i in range(n):
    tree[i + l // 2] = s[i][1]
y = [n - 1] * n
j = 0
for i in range(n):
    if j == n:
        break
    while True:
        if j == n:
            break
        if s[i][0] + 2 * d >= s[j][0]:
            j += 1
        else:
            y[i] = j - 1
            break
ans = 0
for i in range(n):
    h = get(i)
    if h > 0:
        c = math.ceil(h / a)
        ans += c
        update(i, y[i], -1 * a * c)
print(ans)