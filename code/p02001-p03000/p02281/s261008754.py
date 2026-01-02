n=int(input())
p_list=[-1]*n
s_list=[-1]*n
c_list=[0]*n
degree=[0]*n
depth=[0]*n
height=[0]*n
type=[0]*n
for _ in range(n):
    id,l,r=map(int,input().split())
    c_list[id]=[l,r]
    if l!=-1 and r!=-1:
        degree[id]=2
        type[id]="internal node"
        p_list[l]=id
        p_list[r]=id
        s_list[l]=r
        s_list[r]=l
    elif r!=-1:
        degree[id]=1
        type[id]="internal node"
        p_list[r]=id
        s_list[r]=l
    elif l!=-1:
        degree[id]=1
        type[id]="internal node"
        p_list[l]=id
        s_list[l]=r
    else:
        degree[id]=0
        type[id]="leaf"
root=p_list.index(-1)
type[root]="root"

pre=[]
def dsf1(v):
    pre.append(v)
    if c_list[v]!=[-1,-1]:
        if c_list[v][0]==-1:
            dsf1(c_list[v][1])
        elif c_list[v][1]==-1:
            dsf1(c_list[v][0])
        else:
            dsf1(c_list[v][0])
            dsf1(c_list[v][1])
dsf1(root)

inn=[]
def dsf2(v):
    if c_list[v][0]!=-1:
        dsf2(c_list[v][0])
    inn.append(v)
    if c_list[v][1]!=-1:
        dsf2(c_list[v][1])    
dsf2(root)

post=[]
def dsf3(v):
    if c_list[v]!=[-1,-1]:
        if c_list[v][0]==-1:
            dsf3(c_list[v][1])
        elif c_list[v][1]==-1:
            dsf3(c_list[v][0])
        else:
            dsf3(c_list[v][0])
            dsf3(c_list[v][1])
    post.append(v)
dsf3(root)
print("Preorder")
print("",*pre)
print("Inorder")
print("",*inn)
print("Postorder")
print("",*post)
