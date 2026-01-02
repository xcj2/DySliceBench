import sys
input = sys.stdin.readline

class SegmentTree():
    def __init__(self,arr,func=min,ie=2**63-1):
        self.n = 2**(len(arr)-1).bit_length()
        self.ie = ie
        self.func = func
        self.tree = [ie for _ in range(2*self.n)]
        for i in range(len(arr)):
            self.tree[self.n+i-1] = arr[i]
        for i in range(self.n-1)[::-1]:
            self.tree[i] = func(self.tree[2*i+1],self.tree[2*i+2])
    def update(self,index,x): #0-index！
        index += self.n-1
        self.tree[index] = x
        while index>0:
            index = (index-1)//2
            self.tree[index] = self.func(self.tree[2*index+1],self.tree[2*index+2])
    def query(self,left,right): #開区間！
        if right <= left:
            return self.ie
        left += self.n-1
        right += self.n-2
        res = self.ie
        while right-left > 1:
            if left & 1 == 0:
                res = self.func(res,self.tree[left])
            if right & 1 == 1:
                res = self.func(res,self.tree[right])
                right -= 1
            left = left//2
            right = (right-1)//2
        if left == right:
            res = self.func(res,self.tree[left])
        else:
            res = self.func(self.func(res,self.tree[left]),self.tree[right])
        return res

N,Q = map(int,input().split())
ans = []
A = [2**31-1 for _ in range(N)]
sg = SegmentTree(A)
for _ in range(Q):
    c,x,y = map(int,input().split())
    if c==0:
        sg.update(x,y)
    else:
        ans.append(sg.query(x,y+1))
print(*ans,sep='\n')
