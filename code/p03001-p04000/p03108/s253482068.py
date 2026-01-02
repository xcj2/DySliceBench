N,M = map(int, input().split())

class UFT:
    def __init__(self, N):
        self.UFdata = [-1] * (N+1)
        self.rank   = [0]  * (N+1)
        self.connected_num = [1] * (N+1)

    def find(self,x):
        UFdata = self.UFdata
        while UFdata[x] != -1:
            x = UFdata[x]
        return x

    def unite(self,x,y):
        UFdata = self.UFdata
        rank = self.rank
        connected_num = self.connected_num
        find = self.find

        x = find(x)
        y = find(y)
        if x != y:
            if rank[x] < rank[y]:
                UFdata[x] = UFdata[y]
                x,y = y,x
            if rank[x] == rank[y]:
                rank[x] += 1
            UFdata[y] = x       
            connected_num[x] += connected_num[y]
            

UF = UFT(N)

import sys

input = sys.stdin.readline
AB = [ [int(j) for j in input().split()] for _ in range(M)]
AB = list(reversed(AB))

ans = [0] * (M+1)
ans[0] = N*(N-1)//2
for i in range(M):
    a,b = AB[i]
    if UF.find(a) != -1 and  UF.find(a) == UF.find(b):
        ans[i+1] = ans[i]
        continue
        
    cnt1 = UF.connected_num[ UF.find(a) ]   
    cnt2 = UF.connected_num[ UF.find(b) ]  
    UF.unite(a,b)
    # cnt = UF.connected_num[ UF.find(a) ]  -1 
    cnt = cnt1*cnt2

    last = ans[i]
    last -= cnt
    ans[i+1] = last

for i in range(M-1, -1, -1):
    # if ans[i] > 0:
    print(ans[i])
    # else:
    #     print(0)
