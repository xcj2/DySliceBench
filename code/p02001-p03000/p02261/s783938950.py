class Trump(str):
    def __init__(self, card):
        super().__init__()
        self.num = int(card[1])

def trump_bubble_sort(A, N):
    flg = True
    while flg:
        flg = False
        for i in range(1, N):
            if A[i - 1].num > A[i].num:
                A[i], A[i - 1] = A[i - 1], A[i]
                flg = True
    return A


def trump_selection_sort(A, N):
    for i in range(0, N-1):
        min_idx = i
        for j in range(i+1, N):
            if A[min_idx].num > A[j].num:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
        
    return A

N = int(input().rstrip())
A = [Trump(a) for a in input().rstrip().split()]
A_2 = A.copy()

bubble_result = trump_bubble_sort(A, N)
selection_result = trump_selection_sort(A_2, N)

stable = True
for i in range(0, N):
    if bubble_result[i] != selection_result[i]:
        stable = False
        break
print(" ".join(bubble_result))
print("Stable")
print(" ".join(selection_result))
print("Stable" if stable else "Not stable")
    

