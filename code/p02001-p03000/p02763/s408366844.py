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

    def set(self,index,x):
        index += self.n-1
        tree = self.tree
        func = self.func
        tree[index] = x
        while index:
            index = (index-1)//2
            tree[index] = func(tree[2*index+1],tree[2*index+2])

    def query(self,left,right):
        ie = self.ie
        tree = self.tree
        func = self.func
        if right <= left:
            return ie
        left += self.n-1
        right += self.n-2
        tmp_l = self.ie
        tmp_r = self.ie
        while right-left>1:
            if left & 1 == 0:
                tmp_l = func(tmp_l,tree[left])
            if right & 1 == 1:
                tmp_r = func(tree[right],tmp_r)
                right -= 1
            left = left//2
            right = (right-1)//2
        if left == right:
            tmp_l = func(tmp_l,tree[left])
        else:
            tmp_l = func(func(tmp_l,tree[left]),tree[right])
        return func(tmp_l,tmp_r)

import sys
input = sys.stdin.readline

N = int(input())
S = input()
Q = int(input())

A = []
for i in range(N):
    A.append(set([ord(S[i])-97]))

def func(x,y):
    return x|y
ie = set()

st = SegmentTree(A,func,ie)

ans = []

for _ in range(Q):
    q,x,y = input().split()
    q = int(q)
    if q == 1:
        st.set(int(x)-1,set([ord(y)-97]))
    else:
        ans.append(len(st.query(int(x)-1,int(y))))

print('\n'.join(map(str,ans)))