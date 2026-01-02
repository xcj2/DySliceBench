class Node:
    def __init__(self, x, y):
        self.id = x
        self.k = y
        self.children = []
        self.type = ''
        self.depth = 20
        self.parent = '-1'

def findRoot(tree):
    for x in tree:
        for y in x.children:
            tree[int(y)].parent = x.id
            if tree[int(y)].k == 0:
                tree[int(y)].type = 'leaf'
            else:
                tree[int(y)].type = 'internal node'
            '''for a in tree:
                if y == a.id:
                    if a.k == 0:
                        a.type = 'leaf'
                    else:
                        a.type = 'internal node'
                    a.parent = x.id
            '''
    for i,x in enumerate( tree):
        if x.type == 'root':
            return i


def setd(tree,node,d):
    node.depth = d
    if node.k == 0:
        return
    else:
        for tmp in node.children:
            setd(tree,tree[int(tmp)],d+1)
            '''for x in tree:
                if x.id == tmp:
                    setd(tree,x,d+1)
            '''


if __name__ == '__main__':
    n = (int)(input())
    tree = [None]*n
    for i in range(0,n):
        tmp = input().split()
        a = Node(tmp[0],(int)(tmp[1]))
        a.children=tmp[2:]
        a.type = 'root'
        tree[int(a.id)] = a
    ri = findRoot(tree)
    setd(tree,tree[ri],0)
    
    for tmp in tree:
        print("node {}: parent = {}, depth = {}, {}, {}".format(tmp.id, tmp.parent,tmp.depth,tmp.type,list(map(int,tmp.children))))

    