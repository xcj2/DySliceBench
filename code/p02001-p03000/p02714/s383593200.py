def Int():
    return int(input())
def Ints():
    return map(int,input().split())
def IntList():
    return list(Ints())
def IntMat(N):
    return [IntList() for i in range(N)]

N = Int()
S = input()

ans = [0]*8
ans[0] = 1
D = {'R':1, 'G':2, 'B':4}

for i in range(N):
    #print(ans)
    for j in range(8):
        k = 7-j
        if k|D[S[i]] != k:
            ans[k|D[S[i]]] += ans[k]
#print(ans)
tmp = 0
for i in range(N):
    for j in range(1,N):
        if i+2*j < N:
            if S[i]!=S[i+j] and S[i] != S[i+2*j] and S[i+j] != S[i+2*j]:
                tmp += 1
print(ans[7]-tmp)