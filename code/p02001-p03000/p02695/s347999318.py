import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M,Q=MI()
    a=[0]*Q
    b=[0]*Q
    c=[0]*Q
    d=[0]*Q
    
    for i in range(Q):
        a[i],b[i],c[i],d[i]=MI()
    
    #dfsの数列生成
    st=[]
    st2=[]
    for i in range(1,M+1):
        st.append([i])
    
    for dig in range(N):
        while len(st)!=0:
            L=st.pop()
            v=L[-1]
            for i in range(v,M+1):
                st2.append(L+[i])
                
        while len(st2)!=0:
            L=st2.pop()
            st.append(L)
            
    ans=0
    for i in range(len(st)):
        L=st[i]
        temp=0
        for j in range(Q):
            if L[b[j]-1]-L[a[j]-1]==c[j]:
                temp+=d[j]
        ans=max(ans,temp)
    print(ans)
    
    
    
main()
