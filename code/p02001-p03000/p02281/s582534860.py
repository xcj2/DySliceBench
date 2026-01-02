dic, link = (dict() for i in range(2))
n = int(input())
se = set(int(x) for x in range(n))

for i in range(n):
    a, b, c = map(int, input().split())
    link[a] = list()
    for bc in [b, c]:
        link[a].append(bc)
        se.discard(bc)

rt = se.pop()
pre_odr, in_odr, pst_odr = ([] for i in range(3))


def dfs_pr(u):
    pre_odr.append(u)
    for e in link[u]:
        if e >= 0: dfs_pr(e)


def dfs_in(u):
    for i in range(2):
        if i < len(link[u]):
            if i != 0 and u not in used:
                in_odr.append(u)
                used.add(u)
            e = link[u][i]
            if e < 0: continue
            dfs_in(e)
            if e not in used:
                in_odr.append(e)
                used.add(e)


def dfs_ps(u):
    for e in link[u]:
        if e >= 0: dfs_ps(e)
    pst_odr.append(u)


print("Preorder")
dfs_pr(rt)
print("", *pre_odr)

print("Inorder")
used = set()
dfs_in(rt)
if len(in_odr) == 0: in_odr.append(0)
print("", *in_odr)

print("Postorder")
dfs_ps(rt)
print("", *pst_odr)

