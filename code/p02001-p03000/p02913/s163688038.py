def Z_algo(S):
    L = len(S)
    lcp = [0]*L
    i = 1
    j = 0
    lcp[0] = L
    while i < L:
        while i+j < L and S[j] == S[i+j]:
            j += 1
        if not j:
            i += 1
            continue
        lcp[i] = j
        k = 1
        while i + k < L and k + lcp[k] < j:
            lcp[i+k] = lcp[k]
            k += 1
        i += k
        j -= k
    return lcp

def max2(x,y):
    return x if x > y else y

def min2(x,y):
    return x if x < y else y

res = 0
N = int(input())
S = input()
for i in range(N):
    lcp = Z_algo(S[i:])
    for j, s in enumerate(lcp):
        temp = min2(s, j)
        res = max2(res, temp)
print(res)