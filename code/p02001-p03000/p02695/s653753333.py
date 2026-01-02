def Int():
    return int(input())
def Ints():
    return map(int,input().split())
def IntList():
    return list(Ints())
def IntMat(N):
    return [IntList() for i in range(N)]

N,M,Q = Ints()
List = []

for i in range(Q):
    a,b,c,d = Ints()
    List.append([a,b,c,d])
    
import itertools
Num = [i for i in range(N+M-1)]
Ans = 0

for i in itertools.combinations(Num, N):
    TMP = []
    now = 1
    pre = -1
    for j in i:
        TMP.append(now+j-pre-1)
        now = now+j-pre-1
        pre = j
    #print(TMP)
    
    Tensuu = 0
    for (a,b,c,d) in List:
        if TMP[b-1]-TMP[a-1] == c:
            Tensuu += d
    Ans = max(Ans, Tensuu)
print(Ans)