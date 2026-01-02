class KMP:
    def partial(self, P):
        ret = [0]
        for i in range(1, len(P)):
            j = ret[i - 1]
            while j > 0 and P[j] != P[i]:
                j = ret[j - 1]
            ret.append(j + 1 if P[j] == P[i] else j)
        return ret

    def search(self, S, P):
        partial, ret, j = self.partial(P), [], 0        
        for i in range(len(S)):
            while j > 0 and S[i] != P[j]:
                j = partial[j - 1]
            if S[i] == P[j]: j += 1
            if j == len(P): 
                ret.append(i - (j - 1))
                j = partial[j - 1]
        return ret

def main():
    S=list(map(ord,input()))
    T=list(map(ord,input()))
    N,M=len(S),len(T)
    I=KMP().search(S*(M//N+2),T)
    A=[False]*N
    B=[False]*N
    C=[0]*N
    for i in I:
        A[i%N]=True
    for i in range(N):
        if B[i]: continue
        B[i]=True
        j=i
        acc=0
        while A[j]:
            j=(j+M)%N
            acc+=1
            if B[j] and A[j]:
                C[i]=C[j]+acc
                break
            C[j]=max(C[j],acc)
            B[j]=True
        if acc and i==j:
            print(-1)
            return
        C[i]=max(C[i],acc)
    print(max(C))

if __name__ == "__main__":
    main()