import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

class Counter:
    def __init__(self):
        self.dict = {}

    def add(self,x):
        if x in self.dict: self.dict[x] += 1
        else: self.dict[x] = 1

    def decrement(self,x):
        self.dict[x] -= 1
        if self.dict[x] <= 0:
            del self.dict[x]

    def get_dict(self):
        return self.dict


INF=10**20
def main():
    N,M=mi()
    A=list(mi())

    X = []
    for i in range(M):
        b,c=mi()
        X.append((c,b))
    
    X.sort(reverse=True)
    A.sort(reverse=True)

    xi = 0
    b = 0

    newA = []
    while A:
        if not xi < len(X): break
        
        if b == 0: c,b = X[xi]
        a = A.pop() # 小さい順に

        # print(a,b,c)
        if a < c:   
            newA.append(c)
        else:
            A.append(a)
            b = 0

        b -= 1 
        if b <= 0:
            xi += 1
    
    # print(A)
    # print(newA)
    print(sum(newA) + sum(A))
        

        




if __name__ == "__main__":
    main()