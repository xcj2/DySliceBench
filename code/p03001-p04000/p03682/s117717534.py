def main():
    import heapq
    from sys import stdin
    input=stdin.readline
    class unionfind():
        #size:要素数,tree：unionfind木
        def __init__(self,size):#self,要素数
            self.size=size
            self.tree=[[i,1] for i in range(self.size)]#root,depth
        
        #rootを探す
        def root(self,index):
            if self.tree[index][0]==index:
                return index
            else:
                self.tree[index][0]=self.root(self.tree[index][0])
                return self.tree[index][0]
    
        #結合
        def unite(self,index1,index2):
            r1=self.root(index1)
            r2=self.root(index2)
            if r1!=r2:
                d1,d2=self.tree[r1][1],self.tree[r2][1]
                if d1<=d2:
                    self.tree[r1][0]=r2
                    self.tree[r2][1]=max(d1+1,d2)
                else:
                    self.tree[r2][0]=r1
                    self.tree[r1][1]=max(d2+1,d1)
    
        #同じか判定
        def same(self,index1,index2):
            r1=self.root(index1)
            r2=self.root(index2)
            return r1==r2
    
    n=int(input())
    xy=[list(map(int,input().split())) for _ in [0]*n]
    xyz=[xy[i]+[i] for i in range(n)]
    x_sort=sorted(xyz,key=lambda x:x[0])
    y_sort=sorted(xyz,key=lambda x:x[1])
    g=[]
    heapq.heapify(g)
    for i in range(n-1):
        heapq.heappush(g,[abs(x_sort[i+1][0]-x_sort[i][0]),x_sort[i][2],x_sort[i+1][2]])
    for i in range(n-1):
        heapq.heappush(g,[abs(y_sort[i+1][1]-y_sort[i][1]),y_sort[i][2],y_sort[i+1][2]])
    u=unionfind(n)
    cnt=0
    while g:
        d,i,j=heapq.heappop(g)
        if u.same(i,j)==False:
            cnt+=d
            u.unite(i,j)
    print(cnt)
main()