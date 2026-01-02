N = int(input())
A = list(input().split())

def val(card):
    return int(card[1])

def bubble_sort(A, N):
    x = A.copy()
    for i in range(N):
        for j in range(N-1, i, -1):
            if val(x[j]) < val(x[j-1]):
                x[j], x[j-1] = x[j-1], x[j]
    return x

def selection_sort(A, N):
    x = A.copy()
    for i in range(N):
        mini = i
        for j in range(i, N):
            if val(x[j]) < val(x[mini]):
                mini = j
        x[i], x[mini] = x[mini], x[i]
    return x
    
A_bubble = bubble_sort(A, N)
A_selection = selection_sort(A, N)

print(' '.join(map(str, A_bubble)))
print("Stable")
print(' '.join(map(str, A_selection)))
if A_bubble == A_selection:
    print("Stable")
else:
    print("Not stable")
