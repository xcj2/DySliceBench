import sys

I = 0
K = 1
C = 2
P = 3
D = 4

def setd(A, id, d):
    n = A[id]
#    print("depth d:{} n:{} {}".format(d,id,n))
    n[D] = d
    if n[K] > 0:
        for c in n[C]:
            setd(A, c, d + 1)

def setp(A, id, pid):
    n = A[id]
#    print("parent n:{} {}".format(id,n))
    if pid > -1:
        n[P] = pid
    if n[K] > 0:
        for c in n[C]:
            setp(A, c, n[I])

def getroot(A, id):
    if A[id][P] > -1:
        return getroot(A,A[id][P])
    return A[id][I]

def main():

    """ ????????? """
    num = int(input().strip())
    istr = sys.stdin.read()
    nlist = list(istr.splitlines())
    
    nodes = [[i,0,None,-1,0] for i in range(num)]

    for nstr in nlist:
        i = list(map(int,nstr.split()))
        id = i[0]
        n = nodes[id]
#        print("set n:{} {}".format(id,n))
        if i[K] != 0:
            n[K] = i[K]
            n[C] = i[2:]
            setp(nodes, i[0], -1)

    r = getroot(nodes, 0)
    setd(nodes,r, 0)

    for id in range(num):
        n = nodes[id]
#        print("print n:{} {}".format(id,n))
        type = "leaf"
        children = ""
        if n[K] > 0:
            type = "internal node"
            children = ", ".join(map(str,n[C]))
        if n[P] == -1:
            type = "root"
        print("node {0}: parent = {1}, depth = {2}, {3}, [{4}]".format(n[I], n[P], n[D], type, children))

if __name__ == '__main__':
    main()