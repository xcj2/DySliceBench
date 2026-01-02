import sys
def maxHeapify(A, i):
    l = i * 2 + 1
    r = i * 2 + 2
    if l < n:
        largest = l
        if r < n and A[r] > A[l]:
            largest = r
        if A[largest] > A[i]:
            A[i], A[largest] = A[largest], A[i]
            maxHeapify(A, largest)
def insert(S, k):
    global n
    S[n] = k
    n += 1
    i = n - 1
    p = (i - 1) // 2
    while i > 0 and S[i] > S[p]:
        S[i], S[p] = S[p], S[i]
        i = p
        p = (i - 1) // 2
def extractMax(S):
    global n
    if n == 1:
        n -= 1
        return S[0]
    ans = S[0]
    n -= 1
    S[0] = S[n]
    i = 0
    while True:
        l = i * 2 + 1
        r = i * 2 + 2
        if l >= n:
            break
        largest = l
        if r < n and A[r] > A[l]:
            largest = r
        if A[largest] > A[i]:
            A[i], A[largest] = A[largest], A[i]
            i = largest
        else:
            break
    return ans
A = [0] * 2000000
S = []
n = 0
for s in sys.stdin:
    if s[2] == "s":
        insert(A, int(s[7:]))
    elif s[2] == "t":
        S.append(extractMax(A))
    else:
        break
print("\n".join(map(str, S)))

