I = 0
L = 1
R = 2
P = 3
B = 4
D = 5
H = 6

def getidx(Tree,value):
    idx = -1
    for i in range(len(Tree)):
        if Tree[i][I] == value:
            idx = i
            break
    return idx

def search(Tree, A, B, num):
    root = A[0]
    rootidx = getidx(Tree,root)
    ld = num
    for i in range(num):
        if B[i] == root:
            ld = i
            break
    if ld > 0:
        left,lidx = search(Tree,A[1:ld+1],B[:ld],ld)
        Tree[rootidx][L] = lidx
    rt = ld + 1
    if rt < num:
        right,ridx = search(Tree,A[rt:],B[rt:],num - rt)
        Tree[rootidx][R] = ridx
    return (root,rootidx)

def postorder(Tree, nidx, A):
    if nidx < 0:
        return
    postorder(Tree,Tree[nidx][L],A)
    postorder(Tree,Tree[nidx][R],A)
    A.append(Tree[nidx][I])


def main():

    """ ????????? """
    num = int(input().strip())
    plist = list(map(int,input().split()))
    ilist = list(map(int,input().split()))
    tree = []
    for i in plist:
        tree.append([i, -1, -1, -1, -1, 0, 0])

    root,ridx = search(tree, plist, ilist, num)

    pos = []

    postorder(tree, ridx, pos)
    print(" ".join(map(str,pos)))

if __name__ == '__main__':
    main()