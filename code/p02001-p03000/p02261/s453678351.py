def select(S):
    for i in range(0, n):
        minj = i
        for j in range(i, n):
            if int(S[j][1]) < int(S[minj][1]):
                minj = j
        (S[i], S[minj]) = (S[minj], S[i])
    return S

def bubble(B):
    flag = True
    while flag:
        flag = False
        for j in reversed(range(1, n)):
            if int(B[j][1]) < int(B[j-1][1]):
                (B[j-1], B[j]) = (B[j], B[j-1])
                flag = True
    return B

def isStable(inA, out):
    for i in range(0, n):
        for j in range(i+1, n):
            for a in range(0, n):
                for b in range(a+1, n):
                    if inA[i][1] == inA[j][1] and inA[i] == out[b] and inA[j] == out[a]:
                        return "Not stable"
    return "Stable"



n = int(input())
A = input().split(' ')

B = bubble(A[:])
print(" ".join(B))
print(isStable(A, B))
S = select(A[:])
print(" ".join(S))
print(isStable(A, S))