import copy

class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.view = self.suit + str(self.number)

def bubble_sort(A):
    count = 0
    while True:
        swapped = False
        for i in range(len(A)-1):
            if A[i+1].number < A[i].number:
                A[i+1], A[i] = A[i], A[i+1]
                count += 1
                swapped = True
        if not swapped:
            return count

def selection_sort(A):
    count = 0
    for i in range(len(A)):
        min_value = A[i].number
        min_value_index = i
        # print('- i:', i, 'A[i]', A[i], '-')
        for j in range(i, len(A)):
            # print('j:', j, 'A[j]:', A[j])
            
            if A[j].number < min_value:
                min_value = A[j].number
                min_value_index = j
        # print('min_value', min_value, 'min_value_index', min_value_index)
        if i != min_value_index:
            count += 1
            A[i], A[min_value_index] = A[min_value_index], A[i]
            # print('swap!', A)
        
    return count

n = int(input())
A = []
for row in input().split():
    suit, number = list(row)
    A.append(Card(suit, int(number)))

def is_stable(A, B):
    N = len(A)
    for i_A in range(N-1):
        for j_A in range(i_A+1, N):
            for i_B in range(N-1):
                for j_B in range(i_B+1, N):
                    if A[i_A].number == A[j_A].number and A[i_A].view == B[j_B].view and A[j_A].view == B[i_B].view:
                        return False

    return B

bubble_sort_A = copy.deepcopy(A)
selection_sort_A = copy.deepcopy(A)

bubble_sort(bubble_sort_A)
print(*[elem.view for elem in bubble_sort_A])
if is_stable(A, bubble_sort_A):
    print('Stable')
else:
    print('Not stable')

selection_sort(selection_sort_A)
print(*[elem.view for elem in selection_sort_A])

if is_stable(A, selection_sort_A):
    print('Stable')
else:
    print('Not stable')


