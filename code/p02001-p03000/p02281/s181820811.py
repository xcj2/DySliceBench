def preParse(u):
    if u == NIL:
        return
    print(' {}'.format(u), end='')
    preParse(Left[u])
    preParse(Right[u])


def inParse(u):
    if u == NIL:
        return
    inParse(Left[u])
    print(' {}'.format(u), end='')
    inParse(Right[u])


def postParse(u):
    if u == NIL:
        return
    postParse(Left[u])
    postParse(Right[u])
    print(' {}'.format(u), end='')


NIL = -1
n = int(input())
data = [list(map(int, input().split()))for _ in range(n)]
Parent = [NIL]*n
Right = [None]*n
Left = [None]*n
for i in data:
    Right[i[0]] = i[2]
    Left[i[0]] = i[1]
    if i[2] != NIL:
        Parent[i[2]] = i[0]
    if i[1] != NIL:
        Parent[i[1]] = i[0]
for i in range(n):
    if Parent[i] == NIL:
        root = i
'''
print(root)
print(Parent)
print(Right)
print(Left)
'''
print('Preorder')
preParse(root)
print()
print('Inorder')
inParse(root)
print()
print('Postorder')
postParse(root)
print()
