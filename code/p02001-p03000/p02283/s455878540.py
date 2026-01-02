m = int(input())

l, r = {}, {}

def insertnode(num, x):
    """xには毎回rootを設定（rootから順に比較してし、適した場所に追加）"""
    if num < x:
        if x in l:
            if l[x] != 3000000000:
                insertnode(num, l[x])
            else:
                l[x] = num
                return
        else:
            l[x] = num
            return
    else:
        if x in r:
            if r[x] != 3000000000:
                insertnode(num, r[x])
            else:
                r[x] = num
                return
        else:
            r[x] = num
            return

def inorder(num):
    if num == 3000000000:
        return
    if num in l:
        inorder(l[num])
    else:
        l[num] = 3000000000
        inorder(l[num])
    print(' ' + str(num), end='')
    if num in r:
        inorder(r[num])
    else:
        r[num] = 3000000000
        inorder(r[num])

def preorder(num):
    if num == 3000000000:
        return
    print(' ' + str(num), end='')
    if num in l:
        preorder(l[num])
    else:
        l[num] = 3000000000
        preorder(l[num])
    if num in r:
        preorder(r[num])
    else:
        r[num] = 3000000000
        preorder(r[num])

for i in range(m):
    order = input()
    if i == 0:
        global root
        root = int(order[7:])
        continue
    if order[0] == 'i':
        num = int(order[7:])
        insertnode(num, root)
    else:
        inorder(root)
        print()
        preorder(root)
        print()
