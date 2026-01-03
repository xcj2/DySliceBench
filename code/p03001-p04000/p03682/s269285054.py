def main():
    import heapq
    def root(index):
        if tree[index][0]==index:
            return index
        else:
            tree[index][0]=root(tree[index][0])
            return tree[index][0]

    def unite(index1,index2):
        r1=root(index1)
        r2=root(index2)
        if r1!=r2:
            d1,d2=tree[r1][1],tree[r2][1]
            if d1<=d2:
                tree[r1][0]=r2
                tree[r2][1]=max(d1+1,d2)
            else:
                tree[r2][0]=r1
                tree[r1][1]=max(d2+1,d1)

    def same(index1,index2):
        return root(index1)==root(index2)
    
    n=int(input())
    xy=[list(map(int,input().split())) for _ in [0]*n]
    xyz=[xy[i]+[i] for i in range(n)]
    x_sort=sorted(xyz,key=lambda x:x[0])
    y_sort=sorted(xyz,key=lambda x:x[1])
    
    tree=[[i,1] for i in range(n)]#root,depth
    g=[]
    heapq.heapify(g)
    for i in range(n-1):
        heapq.heappush(g,[abs(x_sort[i+1][0]-x_sort[i][0]),x_sort[i][2],x_sort[i+1][2]])
    for i in range(n-1):
        heapq.heappush(g,[abs(y_sort[i+1][1]-y_sort[i][1]),y_sort[i][2],y_sort[i+1][2]])

    cnt=0
    while g:
        d,i,j=heapq.heappop(g)
        if same(i,j)==False:
            cnt+=d
            unite(i,j)
    print(cnt)
main()