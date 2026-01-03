import sys
readline = sys.stdin.buffer.readline

n = int(readline())
T = list(map(int,readline().split()))
m = int(readline())
PX = [list(map(int,readline().split())) for i in range(m)]

class Input():
    def __init__(self,n,T,m,PX):
        self.n = n
        self.T = T
        self.m = m
        self.PX = PX

class Calc(Input):
    def __call__(self):
        time_sum = self.requre_sum()
        for i in range(self.m):
            substract = self.add_sub(i)
            print(time_sum - substract)
    
    def requre_sum(self):
        return sum(self.T)
    
    def add_sub(self,i):
        return self.T[self.PX[i][0]-1] - self.PX[i][1]


x = Calc(n,T,m,PX)

x()