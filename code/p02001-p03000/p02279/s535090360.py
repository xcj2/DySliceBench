import sys
sys.setrecursionlimit(1000000000)

def main():
    N = int(input())
    node_attr_list = [[int(item) for item in input().split()] for _ in range(N)]

    tree = [[0, -1, 0, False, False] for _ in range(N)] # [node, parent, depth, [*child_node], foot print]
    for node_attr in node_attr_list:
        tree[node_attr[0]][0] = node_attr[0]

        if node_attr[1] != 0:
            tree[node_attr[0]][3] = node_attr[2:]
        else:
            tree[node_attr[0]][3] = False

    def dfs(node, depth, parent, children):
        # print(node, depth, parent, children)
        tree[node][4] = True
        tree[node][1] = parent
        tree[node][2] = depth
        if children:
            for item in children:
                dfs(item, depth+1, node, tree[item][3])
        else:
            return

    def all(iterable):
        for element in iterable:
            if not element[4]:
                return False
        return True

    # print(node_attr_list)

    for i in range(N):
        # print('dfs',i)
        # print(tree)
        for j in range(N):
            tree[j][4] = False
        dfs(i, 0, -1, tree[i][3])
        # print(tree)
        # print(all(tree))
        if all(tree):
            break



    for node in tree:
        print('node {}:'.format(node[0]), end=' ')
        print('parent =', node[1], end=', ')
        print('depth =', node[2], end=', ')
        if node[1] == -1:
            print('root', end=', ')
        elif not node[3]:
            print('leaf', end=', ')
        else:
            print('internal node', end=', ')

        if node[3]:
            print(node[3])
        else:
            print([])

if __name__ == "__main__":
    main()

