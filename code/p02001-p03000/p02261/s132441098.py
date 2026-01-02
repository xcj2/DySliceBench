def compare_cards(a, b):
    return a[1] < b[1]

def bubble(C):
    for i in range(len(C)):
        for j in range(len(C) - 1, i, -1):
            if compare_cards(C[j], C[j - 1]):
                C[j], C[j - 1] = C[j -1], C[j]

def selection(C):
    for i in range(len(C)):
        mini = i
        for j in range(i, len(C)):
            if compare_cards(C[j], C[mini]):
                mini = j
        C[i], C[mini] = C[mini], C[i]

def check_stable(originC, sortedC):
    for i in range(len(originC) - 1):
        if not compare_cards(sortedC[i], sortedC[i + 1]):
            if originC.index(sortedC[i]) > originC.index(sortedC[i + 1]):
                return 'Not stable'
    return 'Stable'

        
N = int(input())
C = input().split()

bubbleC = list(C)
selectionC = list(C)

bubble(bubbleC)
selection(selectionC)

print(*bubbleC)
print(check_stable(C, bubbleC))
print(*selectionC)
print(check_stable(C, selectionC))