import bisect
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

class Accumulation:
    def __init__(self,X,accumfunc,init_val=0):
        self.X = X
        self.accumfunc = accumfunc

        N = len(X)
        v1 = [0] * (N+1)
        v1[0] = init_val

        for i in range(N):
            v1[i+1] = accumfunc(v1[i],X[i])

        self.v1 = v1
    
    # 0-index
    def query(self,l,r):
        return self.v1[r+1] - self.v1[l]
    
    def get_array(self):
        return self.v1

INF=10**20
def main():
    N=ii()
    A=list(mi())
    B = []
    for a in A:
        B.append(a*2)

    def add(x,y): return x+y

    acc = Accumulation(A,add)
    accB = Accumulation(B,add)

    vA = acc.get_array()
    vB = accB.get_array()

    ans = INF
    for j in range(N):
        i1 = bisect.bisect_left(vB,vA[j+1]) - 1 

        Q,P=0,INF
        for di in [-1,0,1]:
            if not 0<= i1+di < N: continue
            q,p = acc.query(i1+di+1,j), acc.query(0,i1+di)
            if abs(p-q) < abs(P-Q):
                Q,P = q,p

        S,R = 0,INF
        i2 = bisect.bisect_left(vB,vA[N]+vA[j+1]) - 1
        for di in [-1,0,1]:
            if not 0<= i2+di < N: continue
            s,r = acc.query(i2+di+1,N-1), acc.query(j+1,i2+di)
            if abs(s-r) < abs(S-R):
                S,R=s,r



        ans = min(ans,abs(max(P,Q,R,S) - min(P,Q,R,S)))


    print(ans)





if __name__ == "__main__":
    main()