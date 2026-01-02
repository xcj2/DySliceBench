import sys
input = sys.stdin.readline

class SegmentTree():
    def __init__(self,arr,func=min,ie=2**63):
        self.n = 2**(len(arr)-1).bit_length()
        self.ie = ie
        self.func = func
        self.tree = [ie for _ in range(2*self.n)]
        for i in range(len(arr)):
            self.tree[self.n+i-1] = arr[i]
        for i in range(self.n-1)[::-1]:
            self.tree[i] = func(self.tree[2*i+1],self.tree[2*i+2])
    def update(self,index,x):
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
A = [0 for _ in range(N)]

st = SegmentTree(A,lambda x,y:x+y,0)
ans = []

for _ in range(Q):
    com,x,y = map(int,input().split())
    if com == 0:
        st.update(x-1,st.query(x-1,x)+y)
    else:
        ans.append(st.query(x-1,y))

print(*ans,sep='\n')
