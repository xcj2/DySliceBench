def make_set(x, disjoint):
    disjoint[x] = x

def find_set(x, disjoint):
    if x not in disjoint.keys():
        make_set(x, disjoint)
    if x != disjoint[x]:
        disjoint[x] = find_set(disjoint[x], disjoint)
    return disjoint[x]

def link(x, y, disjoint):
    disjoint[y] = x

def unite(x, y, disjoint):
    link(find_set(x, disjoint), find_set(y, disjoint), disjoint)

def same(x, y, disjoint):
    if find_set(x, disjoint) == find_set(y, disjoint):
        return 1
    return 0

n, q = list(map(int, input().split()))
com_list = list()
x_list = list()
y_list = list()

for _ in range(q):
    com, x, y = list(map(int, input().split()))
    com_list.append(com)
    x_list.append(x)
    y_list.append(y)

disjoint = dict()

for i in range(q):
    com = com_list[i]
    x = x_list[i]
    y = y_list[i]

    if com == 0:
        unite(x, y, disjoint)
    else:
        print(same(x, y, disjoint))