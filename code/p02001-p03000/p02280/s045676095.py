n = int(input())

"""親情報を入れる'p'、子情報を入れる'c'、深さを記録する'd'の、3つの辞書を作成"""
p, c, d = {}, {}, {}

for i in range(n):
    num, *children = input().split()
    c[num] = children
    for j in c[num]:
        if j != '-1':
            p[j] = num

def checkdepth(num, depth):
    d[num] = depth
    for i in c[num]:
        if i != '-1':
            checkdepth(i, depth+1)

"""高さを調べる関数。heightの引数には常に0を渡す"""
def checkheight(num, height):
    if c[num][0] != '-1':
        h1 = checkheight(c[num][0], height+1)
    else:
        h1 = height
    if c[num][1] != '-1':
        h2 = checkheight(c[num][1], height+1)
    else:
        h2 = height
    return max(h1, h2)

root = (set(c) - set(p)).pop()
p[root] = '-1'
checkdepth(root, 0)

def checksibling(num):
    if p[num] != '-1':
        for i in c[p[num]]:
            if i != '-1' and i != num:
                return i
                break
    return '-1'

def checkdegree(num, degree=0):
    for i in c[num]:
        if i != '-1':
            degree += 1
    return degree

for i in range(n):
    i = str(i)
    sibling = checksibling(i)
    degree = checkdegree(i, 0)
    if p[i] == '-1':
        nodetype = 'root'
    elif degree == 0:
        nodetype = 'leaf'
    else:
        nodetype = 'internal node'
    print('node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}'.format(i, p[i], sibling, degree, d[i], checkheight(i, 0), nodetype))
