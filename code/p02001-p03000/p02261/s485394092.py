def bubble(n, A):
    flag = True
    i = 0
    while (flag):
        flag = False
        for j in reversed(range(i+1, n)):
            if (A[j-1][1] > A[j][1]):
                A[j-1], A[j] = A[j], A[j-1]
                flag = True
        i += 1
    return A

def selection(n, A):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if (A[minj][1] > A[j][1]):
                minj = j
        A[minj], A[i] = A[i], A[minj]
    return A

def judge(A, B):
    for i in range(n):
        if (bubble(n, A)[i] != selection(n, B)[i]):
            return "Not stable"
    return "Stable"

n = int(input())
A = input().split(" ")
B = A.copy()
print (" ".join(bubble(n, A)))
print ("Stable")
print (" ".join(selection(n, B)))
print (judge(bubble(n, A), selection(n, B)))
