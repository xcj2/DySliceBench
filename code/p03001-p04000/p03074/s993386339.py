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

def get_sum(s, t):
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
s = list(input())
t = []
if s[0] == "0":
    t.append(0)
u = s[0]
c = 0
for i in s:
    if i == u:
        c += 1
    else:
        t.append(c)
        u = i
        c = 1
t.append(c)
if s[n - 1] == "0":
    t.append(0)
lt = len(t)
tree = make_tree(lt)
for i in range(lt):
    update(i, t[i])
k = 2 * k + 1
ans = 0
if lt - k > 0:
    for i in range((lt - k) // 2 + 1):
        ans = max(ans, get_sum(2 * i, 2 * (i + (k - 1) // 2)))
else:
    ans = n
print(ans)