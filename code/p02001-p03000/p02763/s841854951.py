"""
E
"""
#treeのiに1を加える
def bit_add(I,k):
    while I<=N:
        tree[k][I]+=1
        I+=I&(-I)

def bit_no_add(I,k):
    while I<=N:
        tree[k][I]-=1
        I+=I&(-I)
        
#0からiまでの合計を帰す
def bit_sum(I,k):
    s=0
    while I>0:
        s+=tree[k][I]
        I-=I&(-I)
    return s

N=int(input())
S=["a"]+list(input())
Q=int(input())
que=[list(input().split()) for i in range(Q)]

alpa=list("abcdefghijklmnopqrstuvwxyz")
tree=[[0]*(N+1) for i in range(len(alpa))]

for i in range(1,N+1):
    j=alpa.index(S[i])
    bit_add(i, j)

for iii in range(Q):
    if que[iii][0]=="1":
        i,c=int(que[iii][1]),que[iii][2]
        j=alpa.index(S[i])
        bit_no_add(i, j)
        S[i]=c
        j=alpa.index(c)
        bit_add(i, j)
    else:
        l,r=que[iii][1],que[iii][2]
        l=int(l)
        r=int(r)
        cnt=0
        for j in range(len(alpa)):
            if bit_sum(l-1, j)==bit_sum(r, j):
                continue
            cnt+=1
        print(cnt)