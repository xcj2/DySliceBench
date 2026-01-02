import sys
sys.setrecursionlimit(10**9)
INF=10**18
def input():
    return sys.stdin.readline().rstrip()

def main():
    def nibutan1(ok,ng,index):
        while abs(ok-ng) > 1:
            mid = (ok + ng) // 2
            if solve1(mid,index):
                ok = mid
            else:
                ng = mid
        return ok
    
    def solve1(mid,index):
        P=S[mid]
        Q=S[index]-S[mid]
        return P<Q

    def nibutan2(ok,ng,index):
        while abs(ok-ng) > 1:
            mid = (ok + ng) // 2
            if solve2(mid,index):
                ok = mid
            else:
                ng = mid
        return ok
    
    def solve2(mid,index):
        P=S[mid]-S[index]
        Q=S[N-1]-S[mid]
        return P<Q
    
    N=int(input())
    A=list(map(int,input().split()))
    S=[A[0]]
    for i in range(N-1):
        S.append(S[i]+A[i+1])
    ans=INF
    for i in range(1,N-1):
        c1=nibutan1(0,i-1,i)
        c2=nibutan2(i,N-2,i)
        if abs(S[c1]-(S[i]-S[c1]))<abs(S[c1+1]-(S[i]-S[c1+1])):
            p,q=S[c1],S[i]-S[c1]
        else:
            p,q=S[c1+1],S[i]-S[c1+1]
        if abs(S[c2]-S[i]-(S[N-1]-S[c2]))<abs(S[c2+1]-S[i]-(S[N-1]-S[c2+1])):
            r,s=S[c2]-S[i],S[N-1]-S[c2]
        else:
            r,s=S[c2+1]-S[i],S[N-1]-S[c2+1]
        ans=min(ans,max(p,q,r,s)-min(p,q,r,s))
    print(ans)
        
        
    
if __name__ == '__main__':
    main()
