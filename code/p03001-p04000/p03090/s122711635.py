n=int(input())
l=[]
def upgrade(edge):
    s=len(edge)
    for i in range(s):
        [a,b]=edge[i]
        edge[i]=[a+1,b+1]

def odd(edge,n):
    for i in range(n-1):
        edge.append([n,i+1])

def even(edge,n):
    upgrade(edge)
    for i in range(1,n):
        edge.append([1,i+1])

def print_edge(edge):
    s=len(edge)
    for i in range(s):
        [a,b]=edge[i]
        print(a,b)

edge=[]
#3
edge.append([1,3])
edge.append([2,3])
for i in range(3,n):
    if i%2==0:
        odd(edge,i+1)
    elif i%2==1:
        even(edge,i)
#
print(len(edge))
print_edge(edge)