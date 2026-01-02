import sys
input=sys.stdin.readline
from string import ascii_lowercase

class BIT(): #1-indexed
    def __init__(self,n): #n: 要素数
        self.size=n
        self.bit=[0]*(n+1)
    def add(self,i,x): #i番目(1-indexed)にxを加算
        while i<=self.size:
            self.bit[i]+=x
            i+=i&-i
    def sum_1_to_i(self,i): #1番目からi番目(含む)までの総和(1-indexed)
        s=0
        while i>0:
            s+=self.bit[i]
            i-=i&-i
        return s
    def sum_i_to_j(self,i,j): #i番目からj番目(含む)までの総和(1-indexed)
        return self.sum_1_to_i(j)-self.sum_1_to_i(i-1)
    def reset(self): #初期化
        self.bit=[0]*(self.size+1)

def main():
    A=ascii_lowercase
    D=dict()
    for i,a in enumerate(A):
        D[a]=i
    n=int(input())
    S=list(input().strip())
    L=[BIT(n) for _ in range(26)]
    for i,s in enumerate(S):
        L[D[s]].add(i+1,1)
    q=int(input())
    for _ in range(q):
        k,a,b=input().split()
        if k=='1':
            i=int(a)-1
            s=S[i]
            L[D[b]].add(i+1,1)
            L[D[s]].add(i+1,-1)
            S[i]=b
        else:
            l=int(a); r=int(b)
            ans=0
            for i in range(26):
                ans+=L[i].sum_i_to_j(l,r)>0
            print(ans)
    
if __name__=='__main__':
    main()