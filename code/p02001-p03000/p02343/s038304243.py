
def makeSet(x):
    global p, rank
    p[x] = x
    rank[x] = 0

def union(x,y):
    link(findSet(x), findSet(y))

def link(x, y):
    global p, rank
    if(rank[x] > rank[y]):
        p[y] = x
    else:
        p[x] = y
        if(rank[x] == rank[y]):
            rank[y] = rank[y] + 1

def findSet(x):
    global p
    if(x != p[x]):
        p[x] = findSet(p[x])
    return p[x]

def isSame(x, y):
    global p
    if(findSet(x) == findSet(y)):
        return True
    else:
        return False

if __name__ == "__main__":
    N, Q = (int(z) for z in input().split())
    p = [None] * N
    rank = [None] * N

    for i in range(N):
        makeSet(i)

    for i in range(Q):
        com_i, x, y = (int(z) for z in input().split())
        if(com_i == 0):
            #print("union")
            union(x, y)
        if(com_i == 1):
            #print("isSame")
            if(isSame(x, y) == False):
                print("0")
            else:
                print("1")

