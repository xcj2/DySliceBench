def search_root(l, n):
    i = n
    while l[i] != i:
        i = l[i]
    return i


def set_root(l, root_index, start_index):
    i = start_index
    while l[i] != root_index:
        tmp = i
        i = l[i]
        l[tmp] = root_index


def func(n):
    return (n * (n - 1)) // 2


node_size, input_size = [int(i) for i in input().split()]

br = []
for _ in range(input_size):
    br.append([int(i) for i in input().split()])

cnt_list = [0]
size_list = [1 for _ in range(node_size + 1)]
node_list = [i for i in range(node_size + 1)]

for i in range(1, input_size + 1):
    node1, node2 = br[-i]

    root1, root2 = search_root(node_list, node1), search_root(node_list, node2)

    if root1 == root2:
        cnt_list.append(cnt_list[-1])
    else:
        cnt_list.append(cnt_list[-1] + (size_list[root1] * size_list[root2]))
        if size_list[root1] < size_list[root2]:
            node_list[root1] = root2
            size_list[root2] += size_list[root1]
        else:
            node_list[root2] = root1
            size_list[root1] += size_list[root2]

val = func(node_size)
for i in cnt_list[::-1][1:]:
    print(val - i)