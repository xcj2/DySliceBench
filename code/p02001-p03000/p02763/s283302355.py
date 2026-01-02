L = list("abcdefghijklmnopqrstuvwxyz")

def num(X):
    return L.index(X)


N = int(input())
S = list(str(input()))
S = [0] + S
Q = int(input())

query = [0] * Q

for i in range(Q):
    query[i] = list(input().split())

#print(query)

###Binary Indexed Tree

#A1 ... AnのBIT(1-indexed)
ABC_BIT = [[0]*(N+1) for i in range(26)]

#print(ABC_BIT)

#A1 ~ Aiまでの和 O(logN)
def BIT_query(alp,idx):
    res_sum = 0
    xx = idx
    while xx > 0:
        res_sum += ABC_BIT[alp][xx]
        xx -= xx&(-xx)
    return res_sum

#Ai += x O(logN)
def BIT_update(alp,idx,x):
    xx = idx
    while xx <= N:
        #print(xx)
        ABC_BIT[alp][xx] += x
        xx += xx&(-xx)
    return

#print(L,S,Q)

for i in range(1,N+1):
    BIT_update(num(S[i]),i,1)
    #print(ABC_BIT)

for i in range(Q):
    if query[i][0] == "1":
        y = int(query[i][1])
        z = query[i][2]
        BIT_update(num(S[y]),y,-1)
        BIT_update(num(z),y,1)
        S[y] = z
    else:
        y = int(query[i][1])
        z = int(query[i][2])
        count = 0
        for k in range(26):
            if BIT_query(k,z) - BIT_query(k,y-1) >= 1:
                count += 1
        print(count) 
