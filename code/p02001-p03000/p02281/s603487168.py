INDEX_LEFT = 0
INDEX_RIGHT = 1


# INPUT
n = int(input())

list_child = [[] for _ in range(n)]
list_parent = [-1 for _ in range(n)]

for _ in range(n):

    id, *C = map(int, input().split())

    list_child[int(id)].extend(C)

    for c in C:
        if c == -1:
            continue

        list_parent[int(c)] = int(id)


# PROCESS
def treewalk_preorder(u):
    if u == -1:
        return

    print(f" {u}", end="")
    treewalk_preorder(list_child[u][INDEX_LEFT])
    treewalk_preorder(list_child[u][INDEX_RIGHT])


def treewalk_inorder(u):
    if u == -1:
        return

    treewalk_inorder(list_child[u][INDEX_LEFT])
    print(f" {u}", end="")
    treewalk_inorder(list_child[u][INDEX_RIGHT])


def postorder_treewalk(u):
    if u == -1:
        return

    postorder_treewalk(list_child[u][INDEX_LEFT])
    postorder_treewalk(list_child[u][INDEX_RIGHT])
    print(f" {u}", end="")


root = list_parent.index(-1)

# OUTPUT
print("Preorder")
treewalk_preorder(root)
print()

print("Inorder")
treewalk_inorder(root)
print()

print("Postorder")
postorder_treewalk(root)
print()
