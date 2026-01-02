def Z_algorithm(S):
    l=len(S)
    A=[0]*l
    A[0]=l
    i=1; j=0
    while i<l:
        while i+j<l and S[j]==S[i+j]:
            j+=1
        if not j:
            i+=1
            continue
        A[i]=j
        k=1
        while l-i>k<j-A[k]:
            A[i+k]=A[k]
            k+=1
        i+=k; j-=k
    return A

def Z_find(txt,pattern):
    lp=len(pattern)
    jointxt=pattern+'-'+txt
    Z=Z_algorithm(jointxt)
    return [Z[i]==lp for i in range(lp+1,len(jointxt))]

def solve(s,t):
    ls=len(s); lt=len(t)
    Judge=Z_find(s*2,t)
    ret=0
    Visited=[-1]*ls
    for i in range(ls) :
        if Judge[i] and Visited[i]==-1:
            idx=i
            cnt=0
            while Judge[idx]:
                if Visited[idx]!=-1:
                    cnt+=Visited[idx]
                    break
                cnt+=1
                Visited[idx]=1
                idx=(idx+lt)%ls
                if idx==i:
                    return -1
            Visited[i]=cnt
            ret=max(ret,cnt)
    return ret

s=input(); t=input()
s*=(len(t)+len(s)-1)//len(s)
print(solve(s,t))