import sys
sys.setrecursionlimit(50000)

def findSet(x,element,weight):
    if(x != element[x]):
        element[x],s = findSet(element[x],element,weight)
        weight[x] += s

    return element[x],weight[x]

def union(x,y,element,weight,w):
    x,wx = findSet(x, element, weight)
    y,wy = findSet(y, element, weight)

    link(x,wx,y,wy,w,element)
    
def link(x,wx,y,wy,z,element):
    z = z + wy - wx

    element[x] = y
    weight[x] = z

n,q = map(int, input().split());

element = [i for i in range(n)]
weight = [0 for i in range(n)]

for i in range(q):
    inp = map(int, input().split());
    inp = list(inp)    

    if(inp[0] == 0):
        x,y,w = inp[1],inp[2],inp[3]
        union(x,y,element,weight,w)
    else:
        x,y = inp[1],inp[2]
        x,wx = findSet(x,element,weight)
        y,wy = findSet(y,element,weight)

        if(x == y):
            print(wx - wy)
        else:
            print('?')

