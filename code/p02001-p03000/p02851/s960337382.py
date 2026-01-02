import math
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

class Counter:
    def __init__(self):
        self.dict = {}

    def add(self,x):
        if x in self.dict: self.dict[x] += 1
        else: self.dict[x] = 1

    def decrement(self,x):
        self.dict[x] -= 1

    def get_dict(self):
        return self.dict



INF=10**20
def main():
    N,K=mi()
    A=list(mi())

    def madd(x,y): return (x+y) % K
    V = Accumulation(A,madd)

    v = V.get_array()
    u = [-1] * (N+1)

    for i in range(N+1):  
        u[i] = v[i] - i
        u[i] %= K  
    
    # print(u)
    if K <= N:
        s = u[:K]
        counter = Counter()
        for i in range(K):
            _s = s[i]
            counter.add(_s)

        ans = 0
        current_count = counter.get_dict()
        ans += (current_count[u[0]] - 1)
    
        for i in range(1,N+1):
            # print(u[i:i+K])

            old = u[i-1]
            counter.decrement(old)

            if i+K-1 < len(u):
                new = u[i+K-1] 
                counter.add(new)

            current_count = counter.get_dict()
            ans += (current_count[u[i]] - 1)
            # print(i,current_count[u[i]] - 1)
        
        print(ans)


    else:
        counter = Counter()
        for i in range(N+1):
            counter.add(u[i])
        
        u = counter.get_dict()
        ans = 0
        for c in u.values():
            if c <= 0: continue
            ans += c*(c-1)//2
        
        print(ans)
            
    


if __name__ == "__main__":
    main()
