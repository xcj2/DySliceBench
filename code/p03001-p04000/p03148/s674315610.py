def Int():
    return int(input())
def Ints():
    return map(int,input().split())
def IntList():
    return list(Ints())
def IntMat(N):
    return [IntList() for i in range(N)]

import sys
sys.setrecursionlimit(4100000)
input = sys.stdin.readline

N,K = Ints()
ALL = []
NetaMax = 0
MaxNeta = {}

for i in range(N):
    t,d = Ints()
    ALL.append([d,t])
    if not t in MaxNeta:
        NetaMax += 1
        MaxNeta[t] = d
    else:
        MaxNeta[t] = max(MaxNeta[t], d)
    
ALL.sort()
ALL = ALL[::-1]
NetaBest = []

for i in MaxNeta:
    NetaBest.append(MaxNeta[i])
    
NetaBest.sort()
NetaBest = NetaBest[::-1]

ans = 0
tmpans = 0
count = 0
tmpD = {}
Second = []

for i in range(K):
    d, t = ALL[i]
    if not t in tmpD:
        tmpD[t] = 1
        count += 1
    else:
        Second.append(d)
    tmpans += d

Second.sort()
#print(Second, count)
ans = tmpans + count**2
#print(NetaBest)

for i in range(count+1, min(K, NetaMax)+1):
    #print(i,i - (count+1))
    tmpans -= Second[i - (count+1)]
    tmpans += NetaBest[i-1]
    #print(tmpans + i**2)
    ans = max(ans, tmpans + i**2)
    
print(ans)