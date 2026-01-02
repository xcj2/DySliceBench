import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

class BitSum:
    def __init__(self, n):
        self.n = n + 1
        self.table = [0] * self.n

    def add(self, i, x):
        i += 1
        while i < self.n:
            self.table[i] += x
            i += i & -i

    def sum(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.table[i]
            i -= i & -i
        return res

n,q=MI()
cc=LI()
lri=[]
mx=500005
#mx=10
for i in range(q):
    l,r=MI()
    l-=1
    lri.append((l,r-1,i))

lri.sort(key=lambda x:x[1])

#print(lri)
last=[-1]*mx
st=BitSum(mx)
ans=[0]*q
now=0
for l,r,i in lri:
    for j in range(now,r+1):
        c=cc[j]
        pre=last[c]
        if pre!=-1:st.add(pre,-1)
        last[c]=j
        st.add(j,1)
    #print(l,r,st.tree,last)
    now=r+1
    ans[i]=st.sum(r)-st.sum(l-1)
print(*ans,sep="\n")

