class BITree:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def total(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
N=int(input())
A=[int(input())*(10**5)-i for i in range(N)]
#追加削除
#二分検索
B=[0]+sorted(list(set([i for i in A])))
M=len(B)
D=dict()
for i in range(M):
    D[B[i]]=i
#print(B)
S=BITree(M)
def search(X):
    Y=D[X]
    tmp=S.total(Y)
    if tmp!=S.total(Y-1):
        return Y
    left=0
    right=Y-1
    mid=(left+right)//2
    while(left<=right):
        mid=(left+right)//2
        if S.total(mid)<tmp:
            left=mid+1
        else:
            right=mid-1
    return left
for i in range(N):
    #print([S.total(i+1)-S.total(i) for i in range(M)])
    #print([S.total(i) for i in range(M+1)])
    tmp2=search(A[i])
    if tmp2==0:
        S.add(D[A[i]],1)
    else:
        S.add(D[A[i]],1)
        S.add(tmp2,-1)
print(S.total(M))