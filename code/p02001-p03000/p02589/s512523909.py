class SparseTable():
    def __init__(self,A):
        N=len(A)
        n=N.bit_length()
        self.table=[[-1 for i in range(n)] for i in range(N)]

        for i in range(N):
            self.table[i][0]=A[i]

        for j in range(1,n):
            for i in range(0,N-2**j+1):
                f=self.table[i][j-1]
                s=self.table[i+2**(j-1)][j-1]
                self.table[i][j]=min(f,s)

    def query(self,s,t):
        b=t-s+1
        m=b.bit_length()-1
        return min(self.table[s][m],self.table[t-2**m+1][m])

class BIT():
    def __init__(self,n):
        self.BIT=[0]*(n+1)
        self.num=n

    def query(self,idx):
        res_sum = 0
        while idx > 0:
            res_sum += self.BIT[idx]
            idx -= idx&(-idx)
        return res_sum

    #Ai += x O(logN)
    def update(self,idx,x):
        while idx <= self.num:
            self.BIT[idx] += x
            idx += idx&(-idx)
        return

alphabetlist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
dic={i:e for e,i in enumerate(alphabetlist)}


import sys

input=sys.stdin.readline

N=int(input())
S=[input().rstrip() for i in range(N)]
for i in range(N):
    temp=[S[i][-j-1] for j in range(len(S[i]))]
    S[i]="".join(temp)
S.sort()

def Solve(S):
    exact=[0 for i in range(N)]
    for i in range(1,N):
        id=0
        limit=min(len(S[i]),len(S[i-1]))
        while limit>id and S[i][id]==S[i-1][id]:
            id+=1
        exact[i]=id

    lastappear=[[-1 for i in range(26)] for j in range(N)]
    for i in range(N):
        for j in range(len(S[i])):
            id=dic[S[i][j]]
            lastappear[i][id]=j

    Sparse=SparseTable(exact)

    def cond(s,n,val):
        if n==N or s==-1:
            return False
        check=Sparse.query(s,n)
        return check>=val

    query=[]
    bit=[BIT(N) for i in range(26)]
    res=-N
    for i in range(N):
        L,R=i+1,i+1
        if i!=N-1 and exact[i+1]>=len(S[i])-1:
            start=i+1
            end=N
            while end-start>1:
                test=(end+start)//2
                if cond(i+1,test,len(S[i])-1):
                    start=test
                else:
                    end=test
            R=start+1
        if i!=0 and exact[i]>=len(S[i])-1:
            start=-1
            end=i
            while end-start>1:
                test=(end+start)//2
                if cond(test,i,len(S[i])-1):
                    end=test
                else:
                    start=test
            L=end
        query.append((len(S[i])-1,L,R,dic[S[i][-1]]))
        for j in range(26):
            if lastappear[i][j]!=-1:
                query.append((lastappear[i][j],N+1,i+1,j))

    query.sort(reverse=True)

    for val,l,r,id in query:
        if l==N+1:
            bit[id].update(r,1)
        else:
            res+=bit[id].query(r)-bit[id].query(l-1)
    return res

ans=0
ans+=Solve(S)
print(ans)
