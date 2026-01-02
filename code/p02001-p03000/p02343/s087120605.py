import sys

def findset(x,element):
    if(x != element[x]):
        element[x] = findset(element[x],element)
    return element[x]

def union(x,y,rank,element):
    link(findset(x,element),findset(y,element),rank,element)

def link(x,y,rank,element):
    if(rank[x] > rank[y]):
        element[y] = x
    else:
        element[x] = y
        if(rank[x] == rank[y]):
            rank[y]+=1

n,q = map(int, input().split());

element = [i for i in range(n)]
rank = [0 for i in range(n)]

for i in range(q):
    query,x,y = map(int, input().split());
    if(query == 0):
        union(x,y,rank,element)
    else :
        if(findset(x,element) == findset(y,element)):
            print(1)
        else:
            print(0)
