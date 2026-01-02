
class Node:
    def __init__(self):
        self.left = -1
        self.right = -1
        self.p = -1

def main():
    n = int(input())
    t = [Node() for _ in range(n)]
    for _ in range(n):
        a,b,c = map(int,input().split())
        t[a].left = b
        t[a].right = c
        if b!=-1:t[b].p = a
        if c!=-1:t[c].p = a

    def preorder(i):
        print (' %d'%i,end='')
        if t[i].left!=-1:preorder(t[i].left)
        if t[i].right!=-1:preorder(t[i].right)

    def inorder(i):
        if t[i].left!=-1:inorder(t[i].left)
        print (' %d'%i,end='')
        if t[i].right!=-1:inorder(t[i].right)

    def postorder(i):
        if t[i].left!=-1:postorder(t[i].left)
        if t[i].right!=-1:postorder(t[i].right)
        print (' %d'%i,end='')

    root = -1
    for i in range(n):
        if t[i].p==-1:root = i
    
    print ('Preorder')
    preorder(root)
    print ()

    print ('Inorder')
    inorder(root)
    print ()

    print ('Postorder')
    postorder(root)
    print ()




if __name__ == '__main__':
    main()


