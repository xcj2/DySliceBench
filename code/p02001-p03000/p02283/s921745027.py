def preorder(T, index):
    print(" %d" %T[index][3], end="")
    if T[index][1] != -1:
        preorder(T, T[index][1])
    if T[index][2] != -1:
        preorder(T, T[index][2])


def inorder(T, index):
    if T[index][1] != -1:
        inorder(T, T[index][1])
    print(" %d" %T[index][3], end="")
    if T[index][2] != -1:
        inorder(T, T[index][2])

def insert(T, z):
    if len(T) == 0:
        T.append([0, -1, -1, z])
    else:
        i = 0
        T.append([0, -1, -1, z])
        while True:
            if T[i][3] > z and T[i][1] == -1:
                T[i][1] = len(T) - 1
                T[-1][0] = i
                break
            elif T[i][3] < z and T[i][2] == -1:
                T[i][2] = len(T) - 1
                T[-1][0] = i
                break
            elif T[i][3] > z:
                i = T[i][1]
            elif T[i][3] < z:
                i = T[i][2]


n = int(input())
a = [input().split() for _ in range(n)]

ans = []
for i in a:
    if i[0] == 'insert':
        insert(ans, int(i[1]))
    else:
        inorder(ans, 0)
        print("")
        preorder(ans, 0)
        print("")




