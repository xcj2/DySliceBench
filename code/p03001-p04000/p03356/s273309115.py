def root(x, parent_list):
    if parent_list[x] == x:
        return parent_list[x]
    else:
        parent_list[x] = root(parent_list[x], parent_list)
        return parent_list[x]


def same(x, y, parent_list):
    return root(x, parent_list) == root(y, parent_list)


def unite(x, y, parent_list):
    x = root(x, parent_list)
    y = root(y, parent_list)
    if x == y:
        return

    parent_list[x] = y

N, M = [int(elem) for elem in input().split(' ')]
p_list = [int(elem) - 1 for elem in input().split(' ')]

swap_list = [[int(elem) - 1 for elem in input().split(' ')]\
            for _ in range(M)]

parent_list = list(range(N))
for swap in swap_list:
    unite(swap[0], swap[1], parent_list)

count = 0
for i in range(N):
    if root(p_list[i], parent_list) == root(i, parent_list):
        count += 1

print(count)
